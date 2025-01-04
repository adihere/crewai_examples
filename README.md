# CrewAI Content Generation Project

This project uses CrewAI to generate content through a collaborative process involving multiple AI agents. The system plans, writes, and edits blog posts on specified topics using OpenAI's GPT-3.5-turbo model.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Agents and Tasks](#agents-and-tasks)
- [Logging](#logging)

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root directory based on the `file.env.example` template.
2. Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

To run the content generation process:

```bash
python l2_research_write_article.py
```

The script will generate a blog post on the topic "AGILE IS DEAD IN THE ENTERPRISE" by default. To change the topic, modify the `topic` variable in the script.

## Project Structure

- `l2_research_write_article.py`: Main script containing the CrewAI setup and execution logic.
- `requirements.txt`: List of Python package dependencies.
- `file.env.example`: Template for the environment variables file.

## Agents and Tasks

The project uses three AI agents:

1. **Content Planner**: Plans the content structure and gathers relevant information.
2. **Content Writer**: Writes the blog post based on the planner's outline.
3. **Editor**: Proofreads and refines the final content.

Each agent is assigned specific tasks:

- **Plan**: Develop a content plan with trends, audience analysis, and SEO keywords.
- **Write**: Craft a compelling blog post using the content plan.
- **Edit**: Proofread and align the post with the organization's style.

## Logging

The script uses Python's `logging` module to capture information about the CrewAI process. Logs include:

- Start and completion of the CrewAI process
- Successful result obtainment
- Any errors that occur during execution

Logs are displayed in the console with timestamps and log levels.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/7454916/2d24dd03-c777-4201-91ec-699ffe0b9adb/l2_research_write_article.py
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/7454916/54dc75cc-fb3c-4664-9eb9-1c3e8246b0ca/file.env.example
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/7454916/912f4efb-e761-47f7-a68b-894f1da4906e/requirements.txt
