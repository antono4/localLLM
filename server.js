/**
 * Simple Chat Server for AI Assistant
 * 
 * Usage:
 *   1. npm init -y
 *   2. npm install express cors node-fetch
 *   3. node server.js
 *   4. Buka index.html di browser
 */

const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Serve static files
app.use(express.static('.'));

// Chat endpoint
app.post('/api/chat', async (req, res) => {
    try {
        const { message, history, apiKey } = req.body;
        
        if (!message) {
            return res.status(400).json({ error: 'Message is required' });
        }
        
        if (!apiKey) {
            return res.status(400).json({ error: 'API key is required' });
        }
        
        // Build messages array
        const messages = [
            { role: 'system', content: 'Kamu adalah AI assistant yang helpful. Selalu jawab dalam Bahasa Indonesia.' }
        ];
        
        // Add history
        if (history && history.length > 0) {
            messages.push(...history);
        }
        
        // Add current message
        messages.push({ role: 'user', content: message });
        
        // Call OpenAI API
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo',
                messages: messages,
                max_tokens: 1000,
                temperature: 0.7
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error?.message || `API Error: ${response.status}`);
        }
        
        const data = await response.json();
        const aiResponse = data.choices[0]?.message?.content || 'Maaf, saya tidak bisa memproses request ini.';
        
        res.json({ response: aiResponse });
        
    } catch (error) {
        console.error('Chat error:', error);
        res.status(500).json({ error: error.message || 'Internal server error' });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🤖 AI Chat Server Running!                              ║
║                                                           ║
║   Server: http://localhost:${PORT}                          ║
║                                                           ║
║   1. Buka http://localhost:${PORT} di browser              ║
║   2. Masukkan OpenAI API Key                             ║
║   3. Klik Connect dan mulai chat!                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    `);
});
