<h1>📈 News Search Tool</h1>
A <strong>powerful AI-powered news analysis tool</strong> that extracts and processes content from news articles to answer your questions using Google Gemini AI.

<h2>✨ Features</h2>
<strong>Multi-URL Processing</strong>: Extract content from up to 3 news article URLs simultaneously

<strong>AI-Powered Q&A</strong>: Uses Google's Gemini AI to answer questions based on news content

<strong>Web Scraping</strong>: Automatically extracts text content from news articles

<strong>Vector Search</strong>: FAISS vector database for efficient similarity search

<strong>Source Attribution</strong: Shows which articles were used for each answer

<strong>Streamlit Interface</strong>: User-friendly web application

<h2>🚀 Quick Start</h2>
<h3>Prerequisites</h3>
<strong>Python 3.8+</strong>

<strong>Google API Key</strong> (for Gemini AI)

<strong>Internet Connection</strong> (for web scraping)

<h3>Installation</h3>
<strong>Clone the repository</strong>:

bash
git clone <your-repo-url>
cd <your-repo-directory>
<strong>Install dependencies</strong>:

bash
pip install -r requirements.txt
<strong>Set up environment variables</strong>:

Create a <code>.env</code> file

Add your API key: <code>GOOGLE_API_KEY=your_google_api_key_here</code>

<h2>📁 Project Structure</h2>
<pre> ├── 📄 main.py # Streamlit web interface ├── 📄 requirements.txt # Python dependencies ├── 📄 .env # Environment variables └── 📁 faiss_index_gemini/ # Vector store (auto-generated) </pre>
<h2>🛠️ Configuration</h2>
<h3>AI Model Settings</h3>
<strong>AI Model</strong>: Gemini-2.0-flash (Google)

<strong>Temperature</strong>: 0.9 (creative responses)

<strong>Embeddings</strong>: models/embedding-001 (Google)

<strong>Vector Store</strong>: FAISS

<h3>Text Processing</h3>
<strong>Chunk Size</strong>: 1000 characters

<strong>Separators</strong>: Paragraphs, lines, sentences

<strong>Metadata</strong>: Source URL tracking

<h2>🎯 Usage</h2>
<h3>Running the Application</h3>
bash
streamlit run main.py
<h3>Access the Interface</h3>
Open your browser and navigate to: <code>http://localhost:8501</code>

<h3>Step-by-Step Process</h3>
<strong>Enter URLs</strong>: Input up to 3 news article URLs in the sidebar

<strong>Process Content</strong>: Click "Process URLs" to extract and index content

<strong>Ask Questions</strong>: Type your question in the main input field

<strong>Get Answers</strong>: Receive AI-generated answers with source attribution

<h3>Example Questions</h3>
"What are the main points discussed in these articles?"

"Compare the perspectives from different sources"

"What statistics or data are mentioned?"

"What are the key conclusions?"

<h2>🔧 How It Works</h2>
<strong>URL Processing</strong>: Extracts text content from news articles using web scraping

<strong>Text Splitting</strong>: Divides content into manageable chunks for processing

<strong>Vector Embeddings</strong>: Converts text into numerical representations

<strong>Vector Storage</strong>: Stores embeddings in FAISS for efficient retrieval

<strong>Question Answering</strong>: Uses Gemini AI to generate answers based on retrieved content

<strong>Source Attribution</strong>: Identifies which articles contributed to the answer

<h2>📋 Key Components</h2>
<h3>Web Scraping</h3>
Uses <code>BeautifulSoup</code> for HTML parsing

Extracts paragraph content from news articles

Handles HTTP requests with proper headers and timeouts

<h3>Text Processing</h3>
<strong>RecursiveCharacterTextSplitter</strong>: Splits text intelligently

<strong>Chunk Size</strong>: 1000 characters for optimal processing

<strong>Metadata Preservation</strong>: Maintains source URL information

<h3>AI Integration</h3>
<strong>GoogleGenerativeAIEmbeddings</strong>: Creates text embeddings

<strong>ChatGoogleGenerativeAI</strong>: Generates answers using Gemini

<strong>RetrievalQAWithSourcesChain</strong>: Combines retrieval with Q&A

<h2>⚙️ Technical Details</h2>
<h3>Dependencies</h3>
Key packages include:

<code>streamlit</code>

<code>langchain-google-genai</code>

<code>langchain-community</code>

<code>langchain-core</code>

<code>beautifulsoup4</code>

<code>requests</code>

<code>faiss-cpu</code>

<h3>File Structure</h3>
text
📁 project/
├── 📄 main.py                 # Main application
├── 📄 requirements.txt        # Dependencies
├── 📄 .env                   # Environment variables
└── 📁 faiss_index_gemini/    # Auto-generated vector store
<h2>⚠️ Important Notes</h2>
<strong>API Key Security</strong>: Never commit your <code>.env</code> file to version control

<strong>Web Scraping Ethics</strong>: Respect robots.txt and terms of service

<strong>Rate Limiting</strong>: Be mindful of request frequency to websites

<strong>Content Copyright</strong>: Use extracted content responsibly

<h3>Legal Considerations</h3>
Ensure you have rights to scrape the target websites

Respect copyright and fair use policies

Attribute content properly to original sources

<h2>🆘 Troubleshooting</h2>
<h3>Common Issues</h3>
<strong>URL Loading Errors</strong>: Check internet connection and URL validity

<strong>API Key Issues</strong>: Verify Google API key is valid

<strong>Module Errors</strong>: Ensure all dependencies are installed

<strong>Scraping Blocks</strong>: Some sites may block automated access

<h3>Error Handling</h3>
The application includes:

Timeout handling for web requests

Error logging for debugging

Graceful failure for individual URL processing

<h2>🚀 Performance Tips</h2>
Use reliable news sources with consistent HTML structure

Limit the number of URLs processed simultaneously

Monitor API usage to avoid quota limits

Clear the vector store (<code>faiss_index_gemini</code>) when updating content

