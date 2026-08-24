# Personal AI Assistant (Claude-like)

A conversational AI assistant built from scratch, featuring natural language understanding, multi-turn conversations, and helpful responses.

## Features

- 🤖 **Conversational AI** - Natural dialogue with context awareness
- 💾 **Memory Management** - Maintains conversation history
- 🧠 **Intent Recognition** - Understands user intent and context
- ⚡ **Fast Responses** - Optimized for real-time interaction
- 🔧 **Extensible** - Easy to add new capabilities and integrations
- 📝 **Logging** - Track conversations and performance

## Tech Stack

- **Language**: Python 3.8+
- **ML Framework**: Transformers (HuggingFace)
- **API**: FastAPI for serving
- **Database**: SQLite for conversation history
- **NLP**: NLTK, spaCy

## Project Structure

```
personal-ai-claude/
├── src/
│   ├── ai/
│   │   ├── model.py           # Core AI model
│   │   ├── tokenizer.py       # Text preprocessing
│   │   └── response_gen.py    # Response generation
│   ├── api/
│   │   ├── server.py          # FastAPI server
│   │   └── routes.py          # API endpoints
│   ├── memory/
│   │   ├── conversation.py    # Conversation memory
│   │   └── storage.py         # Database operations
│   └── utils/
│       ├── config.py          # Configuration
│       └── logger.py          # Logging setup
├── tests/
│   ├── test_model.py
│   ├── test_api.py
│   └── test_memory.py
├── requirements.txt
├── .env.example
└── main.py                    # Entry point
```

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/Kabilan1997/personal-ai-claude.git
cd personal-ai-claude
pip install -r requirements.txt
```

### 2. Set Up Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

### 3. Run the AI

```bash
python main.py
```

### 4. API Usage

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello, how are you?",
    "conversation_id": "user_123"
  }'
```

## Development

### Run Tests

```bash
pytest tests/
```

### Train Custom Model

```bash
python scripts/train.py --data your_data.json --epochs 10
```

### Interactive CLI

```bash
python scripts/cli.py
```

## API Endpoints

- `POST /chat` - Send a message and get a response
- `GET /conversation/:id` - Retrieve conversation history
- `DELETE /conversation/:id` - Clear conversation
- `POST /train` - Fine-tune model with custom data
- `GET /health` - Health check

## Configuration

Edit `config.py` or `.env` to customize:

- Model size and architecture
- Memory capacity
- Response temperature (creativity)
- API settings

## Roadmap

- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Integration with external APIs (weather, news, etc.)
- [ ] Fine-tuning on custom datasets
- [ ] Web UI
- [ ] Mobile app
- [ ] Advanced reasoning capabilities
- [ ] Persistent learning

## Contributing

Contributions welcome! Please:

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Push and open a PR

## License

MIT License - see LICENSE file

## Support

For issues and questions, open an issue on GitHub or contact the maintainer.

---

**Happy building! 🚀**