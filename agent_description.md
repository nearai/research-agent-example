### Research Agent

The Research Agent is a web-based tool designed to conduct in-depth research on user-defined topics and generate comprehensive reports. It provides a user-friendly interface for initiating research and viewing the results, including the generated report, source URLs, and estimated costs.

#### Functionality

*   **Web Interface:** Offers an interactive web page where users can submit research queries and select the desired report type.
*   **Automated Research:** Utilizes the GPT Researcher library to gather and synthesize information from multiple online sources based on the provided query.
*   **Report Generation:** Creates structured reports, which can be a detailed research report, a resource list, or an outline.
*   **Source and Cost Tracking:** Provides a list of all sources used during the research process and an estimate of the associated costs.
*   **Health Check:** Includes an endpoint to verify the configuration of required API keys.

#### Inputs

*   **HTTP POST to `/research` (via Web UI or API call):**
    *   `query` (string): The specific topic or question for which research is needed.
    *   `report_type` (string, optional): The desired format of the output report. Supported types include "research\_report" (default), "resource\_report", and "outline\_report".
*   **Environment Variables:**
    *   `OPENAI_API_KEY`: Required for authenticating with the OpenAI API, which powers the language model capabilities.
    *   `TAVILY_API_KEY`: Required for authenticating with the Tavily API, used for web search and information retrieval.

#### Outputs

*   **HTTP GET from `/` (Web UI):**
    *   An HTML page (`static/index.html`) providing the user interface.
*   **HTTP POST from `/research` (JSON response):**
    *   `report` (string): The generated research report content, typically in Markdown format.
    *   `sources` (list of strings): A list of URLs from which information was gathered.
    *   `costs` (dictionary): Contains `total_cost` (float) representing the estimated cost of the research.
    *   `num_sources` (integer): The total count of unique sources identified.

#### Prerequisites

*   **API Keys:** Requires valid `OPENAI_API_KEY` and `TAVILY_API_KEY` to be set as environment variables. Without these, the research functionality will not operate.