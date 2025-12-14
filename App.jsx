import { useState } from "react";

export default function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const analyzeRepo = async () => {
    if (!repoUrl) {
      setError("Please enter a GitHub repository URL");
      return;
    }

    setError("");
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch(
        `${import.meta.env.VITE_API_BASE_URL}/analyze?repo_url=${repoUrl}`
      );

      if (!res.ok) {
        throw new Error("API error");
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError("Failed to analyze repository");
    } finally {
      setLoading(false);
    }
  };

  const badgeColor = (score) => {
    if (score >= 70) return "#22c55e";
    if (score >= 40) return "#facc15";
    return "#ef4444";
  };

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>GitHub-Eval</h1>
        <p style={styles.subtitle}>
          AI-powered GitHub repository evaluation using Gemini LLM
        </p>

        <div style={styles.inputGroup}>
          <input
            style={styles.input}
            placeholder="Paste GitHub repository URL"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
          />
          <button style={styles.button} onClick={analyzeRepo}>
            Evaluate
          </button>
        </div>

        {loading && <p style={styles.loading}>Analyzing with Gemini…</p>}
        {error && <p style={styles.error}>{error}</p>}

        {result && (
          <div style={styles.resultCard}>
            <h3>{result.repository}</h3>

            <div
              style={{
                ...styles.badge,
                background: badgeColor(result.analysis.score),
              }}
            >
              {result.analysis.score}/100 · {result.analysis.level}
            </div>

            <p>{result.analysis.summary}</p>

            <h4>Personalized Roadmap</h4>
            <ul>
              {result.analysis.roadmap.map((step, i) => (
                <li key={i}>{step}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background:
      "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
    fontFamily: "Inter, sans-serif",
  },
  card: {
    background: "rgba(255,255,255,0.15)",
    backdropFilter: "blur(20px)",
    padding: "40px",
    borderRadius: "20px",
    width: "100%",
    maxWidth: "720px",
    color: "#f8fafc",
    boxShadow: "0 40px 100px rgba(0,0,0,0.35)",
  },
  title: {
    fontSize: "2.6rem",
    marginBottom: "10px",
  },
  subtitle: {
    color: "#cbd5e1",
    marginBottom: "30px",
  },
  inputGroup: {
    display: "flex",
    gap: "12px",
  },
  input: {
    flex: 1,
    padding: "16px",
    borderRadius: "14px",
    border: "none",
    fontSize: "1rem",
  },
  button: {
    padding: "16px 26px",
    borderRadius: "14px",
    border: "none",
    fontWeight: "600",
    cursor: "pointer",
    background: "linear-gradient(135deg,#38bdf8,#22c55e)",
  },
  loading: {
    marginTop: "20px",
    fontStyle: "italic",
  },
  error: {
    marginTop: "20px",
    color: "#f87171",
  },
  resultCard: {
    marginTop: "30px",
    background: "rgba(255,255,255,0.2)",
    padding: "25px",
    borderRadius: "16px",
  },
  badge: {
    display: "inline-block",
    padding: "10px 20px",
    borderRadius: "999px",
    fontWeight: "700",
    margin: "12px 0",
    color: "#0f172a",
  },
};
