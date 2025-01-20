// api.js
const API_KEY = 'QYB6bZd7llKZnjImNfsWvyhMim0Yz0RP';

export async function createChatSession(externalUserId) {
  try {
    const response = await fetch('https://api.on-demand.io/chat/v1/sessions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': API_KEY,
      },
      body: JSON.stringify({
        pluginIds: [],
        externalUserId: externalUserId,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to create chat session');
    }

    const data = await response.json();
    return data.data.id;
  } catch (error) {
    console.error('Error creating chat session:', error);
    throw error;
  }
}

export async function submitQuery(sessionId, query) {
  try {
    const response = await fetch(`https://api.on-demand.io/chat/v1/sessions/${sessionId}/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': API_KEY,
      },
      body: JSON.stringify({
        endpointId: 'predefined-openai-gpt4o',
        query: query,
        pluginIds: ['plugin-1712327325', 'plugin-1713962163'],
        responseMode: 'sync',
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to submit query');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error submitting query:', error);
    throw error;
  }
}
