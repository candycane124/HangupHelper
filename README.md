# Hangup Helper
## The Problem
Many seniors are especially vulnerable to online scams. According to the FBI Internet Crime Complaint Center, roughly $3.4 billion in total fraud losses were reported by Americans over the age of 60 in 2023, while Nasdaq reported $77.7 billion of global fraud was linked to elderly victims in 2024.

## Our Solution
Hangup Helper is an AI-powered tool that listens to phone conversations, analyzes speech, and detects potential scams in real-time. It provides immediate warnings or guidance, helping users decide whether to continue the call or hang up. It also allows users to look up unknown numbers to check them against a global scam database of over 4 million records, all through an intuitive and simple interface.

## How We Built It
Our web app was built & deployed using Streamlit. We utilized Azure Cognitive Services (Speech SDK) and Google Gemini in order to transcribe and analyze audio, and ScamSearch API to cross-reference phone numbers. We registered a domain name, itsnotyour.biz, using GoDaddy Registry, and used Cloudflare to manage DNS.

## Next Steps
- Create a mobile app version for easier accessibility and real-time scam detection
- Expand our scam call database to improve fraud detection
- Implement a "Do Not Analyze" feature in the mobile app, allowing users to exclude trusted contacts from analysis
- Improve call transcription and scam detection by integrating more advanced AI models
