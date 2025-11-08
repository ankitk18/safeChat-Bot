# SafeChat - Toxicity Filter & Rewriter

**College Project - AI-Powered Text Analysis**

A simple web application that detects toxic messages and rewrites them politely using Google's Gemini AI.

## 🎯 Project Overview

This is a college project demonstrating:

- AI-powered text analysis
- Toxicity detection in social media content
- Automatic text rewriting for better communication
- Web application development with Streamlit

## ✨ Features

### Core Functionality

- **Toxicity Detection**: Identifies harmful content in text messages
- **Smart Rewriting**: Converts toxic messages to polite alternatives
- **Real-time Analysis**: Instant feedback on message safety
- **Multiple Tone Options**: Professional, Friendly, Polite, Formal styles

### User Interface

- Clean, simple design suitable for all users
- Interactive examples to test the system
- Analysis history tracking
- Adjustable sensitivity settings

## 🚀 How to Run

### Prerequisites

- Python 3.7 or higher
- Google API key (free from Google AI Studio)

### Installation Steps

1. **Download the project files**

   ```bash
   # Download all files: safechat.py, requirements.txt, .env
   ```

2. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   - Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add it to the `.env` file:

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the application**

   ```bash
   streamlit run safechat.py
   ```

5. **Open in browser**
   - The app will open at `http://localhost:8501`

## 🎮 How to Use

1. **Enter Text**: Type or paste any message in the text area
2. **Choose Analysis Type**:
   - "Analyze Message" - Check if text is toxic
   - "Analyze & Rewrite" - Get a polite version if needed
3. **Review Results**: See toxicity score and explanation
4. **Try Examples**: Use provided sample texts to test the system

## 📊 What It Detects

- **Harassment**: Bullying and intimidation
- **Hate Speech**: Discriminatory language
- **Threats**: Violent or threatening content
- **Profanity**: Inappropriate language
- **Personal Attacks**: Direct insults

## 🎓 Educational Value

This project demonstrates:

- **AI Integration**: Using Google's Gemini API
- **Web Development**: Building interactive apps with Streamlit
- **Natural Language Processing**: Text analysis and generation
- **User Experience Design**: Creating intuitive interfaces
- **API Management**: Handling external services securely

## 📈 Technical Details

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Google Gemini 2.5 Flash
- **Language**: Python 3.7+
- **Response Time**: ~2 seconds per analysis
- **Accuracy**: ~85% for clear cases

## 🔒 Privacy & Safety

- **No Data Storage**: Messages are not saved permanently
- **Local Processing**: Analysis happens in real-time
- **Educational Use**: Designed for learning purposes
- **Human Oversight**: Results should be reviewed by humans

## 📝 Project Structure

```
safechat-project/
├── safechat.py          # Main application file
├── requirements.txt     # Python dependencies
├── .env                # API key configuration
├── README.md           # This documentation
└── demo_texts.txt      # Sample texts for testing
```

## 🎯 Future Improvements

- Add more languages support
- Implement batch text processing
- Create mobile-friendly interface
- Add user feedback system
- Integrate with social media APIs

## ⚠️ Limitations

- AI detection is not 100% accurate
- May miss context-dependent sarcasm
- Requires internet connection
- Limited to supported languages

## 🤝 Credits

- **Google Gemini AI** for text analysis
- **Streamlit** for web framework
- **Python Community** for open-source libraries

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google AI Documentation](https://ai.google.dev/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

---

**Made with ❤️ for educational purposes**

_This project is designed for learning and demonstration. Please use responsibly and always review AI-generated content._
