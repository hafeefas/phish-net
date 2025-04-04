# Phish-Net: AI-Powered Phone Scam Simulator

An educational tool that uses AI to simulate common phone scams, helping seniors learn to identify and avoid scam calls.

## Features

- Interactive voice conversations with AI-powered scammers
- Multiple scam personas (Tech Support, Grandparent Scam, IRS Scam)
- Real-time speech recognition for natural conversation
- High-quality voice synthesis using ElevenLabs
- Red flag detection for common scam indicators

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your-openai-key
ELEVENLABS_API_KEY=your-elevenlabs-key
```

## Usage

Run the simulator:
```bash
python test_ai_simulator.py
```

Choose a scenario and interact with the AI scammer by speaking into your microphone. The simulator will:
- Play a ringtone when the call starts
- Convert the scammer's responses to realistic speech
- Detect when you mention sensitive information
- Provide warnings about common scam tactics

## API Endpoints

The project includes a FastAPI server with the following endpoints:

- `GET /`: Welcome message
- `GET /personas`: List available scam personas

Run the API server:
```bash
python main.py
```

## Requirements

- Python 3.8+
- OpenAI API key (for GPT-4)
- ElevenLabs API key (for voice synthesis)
- Working microphone for voice input

## Project Overview
Phish-Net is an innovative educational platform designed to help seniors learn about and protect themselves from common cybersecurity threats through interactive experiences and real-world simulations. The platform focuses on two main components: phone call scam detection and phishing email awareness.

## Target Audience
- Senior citizens (65+)
- Caregivers and family members
- Senior living communities
- Community centers

## Key Features

### 1. Phone Call Scam Simulator
- Interactive voice-based scenarios
- Realistic caller ID spoofing demonstrations
- Common scam patterns recognition
- Immediate feedback and learning points
- Voice interface optimized for seniors

### 2. Phishing Email Game
- Interactive email simulation environment
- Real-world phishing email examples
- Progressive difficulty levels
- Visual indicators for suspicious elements
- Large, readable text and high contrast UI

## Technical Architecture

### Backend (FastAPI)
- RESTful API endpoints
- Secure authentication system
- Real-time feedback processing
- Progress tracking
- Analytics dashboard

### Frontend
- Senior-friendly UI design
- High contrast color schemes
- Large text and buttons
- Clear navigation
- Voice interface support

## Learning Objectives
1. Identify common phone scam tactics
2. Recognize phishing email red flags
3. Understand safe online practices
4. Learn how to verify caller authenticity
5. Develop confidence in handling suspicious communications

## Safety Features
- No real personal information required
- Controlled environment for learning
- Clear distinction between simulation and reality
- Emergency contact information readily available
- Progress tracking without sensitive data

## Future Enhancements
- Mobile app version
- Community leaderboards
- Multi-language support
- Integration with senior living communities
- Regular content updates based on new scam patterns

## Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- Virtual environment
- Required dependencies (see requirements.txt)

### Installation
1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Run the application

## Contributing
We welcome contributions! Please see our contributing guidelines for more details.

## License
[License Type] - See LICENSE file for details

## Contact
[Your Contact Information]

---
*This project was developed for [Hackathon Name] with a focus on making cybersecurity education accessible to seniors.* 