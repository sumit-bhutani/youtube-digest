# YouTube Channel Monitor & Analyzer

A fully automated pipeline that monitors 25 curated YouTube channels daily, fetches transcripts for new videos, generates deep research briefs using Claude, and emails a digest to your inbox.

## What It Does

1. **Scans 25 YouTube channels** via RSS feeds (no YouTube API key required)
2. **Finds videos published in the last 24 hours** across all channels
3. **Fetches transcripts** using `youtube-transcript-api`
4. **Analyzes each transcript** with Claude using a structured 5-step research prompt covering executive summary, key insights, time-coded breakdown, structured tables, critical thinking, and strategic reflection
5. **Saves each analysis** as a Markdown file in the `analyses/` directory
6. **Emails a full digest** to your Gmail address

## Channels Monitored

Covers a curated mix of podcasts, tech content, VC/startup, AI/ML, and product channels including: 20VC, a16z, Acquired, All-In, Lenny's Podcast, Lex Fridman, ByteByteGo, The Diary of a CEO, Stanford Engineering, Y Combinator, and more. See `channels.txt` for the full list.

## Setup

### Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables in `.env`:
   ```
   ANTHROPIC_API_KEY=your_key_here
   GMAIL_ADDRESS=your@gmail.com
   GMAIL_APP_PASSWORD=your_app_password
   ```
   To generate a Gmail App Password: Google Account > Security > 2-Step Verification > App Passwords

3. Run manually:
   ```bash
   python analyze_channels.py
   ```

### Automated Daily Run (GitHub Actions)

The workflow at `.github/workflows/youtube_digest.yml` runs every day at 8am UTC.

**Required GitHub Secrets** (Settings > Secrets and Variables > Actions):
- `ANTHROPIC_API_KEY`
- `GMAIL_ADDRESS`
- `GMAIL_APP_PASSWORD`

You can also trigger the workflow manually from the Actions tab using "Run workflow".

## Output

- **Markdown files** saved to `analyses/YYYY-MM-DD_channel_title.md`
- **Email digest** sent to the configured Gmail address with all analyses concatenated

## File Structure

```
Claude Practice/
├── analyze_channels.py   # Main script
├── channels.txt          # 25 channel handles
├── requirements.txt      # Python dependencies
├── .env                  # Secrets (never committed)
├── .gitignore            # Excludes .env and analyses/
└── analyses/             # Generated MD files (gitignored)
```

## Notes

- Videos without available transcripts are skipped automatically
- The `analyses/` directory is gitignored to avoid committing large files locally, but the GitHub Actions workflow commits them to the repo after each run
- The pipeline handles channels gracefully — if a channel's RSS feed cannot be found, it logs and continues
