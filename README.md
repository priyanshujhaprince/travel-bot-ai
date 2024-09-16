Here’s a cool and professional README file for your GitHub repository:

---

# TravelVibe 🌈

Welcome to **TravelVibe**—a vibrant, AI-powered travel assistant designed to make your travel planning both fun and efficient. Whether you're looking for the best flight deals, luxurious hotel stays, or exciting destinations, TravelVibe has you covered!

## 🛠️ Features

- **AI-Powered Recommendations:** Get personalized travel suggestions and information.
- **Interactive Design:** Enjoy a colorful, dynamic user interface with a dark theme and glowing elements.
- **Form-Based Input:** Easily submit your travel-related questions and receive instant responses.

## 📸 Demo

![TravelVibe Demo](./assets/demo.gif) 

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Groq API Key

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/travelvibe.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd travelvibe
   ```

3. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Create a `.env` file in the root directory and add your Groq API key:

   ```
   GROQ_API_KEY=your_groq_api_key
   ```

### Running the App

Start the Streamlit app by running:

```bash
streamlit run app.py
```

The app will open in your default web browser. If it doesn't open automatically, navigate to `http://localhost:8501` to access it.

## 📝 Usage

1. Enter your travel-related question in the input box.
2. Click "🎉 Get the Best Travel Deals!" or press Enter.
3. Receive personalized travel recommendations and information.

## 💡 Customization

Feel free to modify the styles and features according to your preferences. The custom styles are defined in the `app.py` file under the `st.markdown` section.

## 📚 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📑 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/) for creating a fantastic framework for building interactive applications.
- [Groq](https://groq.com/) for providing the AI capabilities for travel recommendations.

## 📞 Contact

For any questions or feedback, feel free to reach out to [priyanshujhaprince@gmail.com).

---

This README provides a clear and engaging overview of your project, making it easy for others to understand and contribute to it. Feel free to adjust any sections to better fit your project and preferences!
