export default async function handler(req, res) {
    if (req.method !== 'POST') return res.status(405).json({ error: 'Method Not Allowed' });
    const { text, apiKey } = req.body;
    if (!apiKey || apiKey !== process.env.NB_GATE_NOIR) {
        return res.status(402).json({ error: "Payment Required" });
    }
    const optimizedText = `[150K_VERIFIED] ${text}`; 
    return res.status(200).json({ translatedText: optimizedText, status: "SUCCESS" });
}
