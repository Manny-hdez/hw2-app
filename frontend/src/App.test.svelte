<script>
  import { render, screen, waitFor } from '@testing-library/svelte';
  import { expect, test, vi, beforeAll, afterEach, afterAll } from 'vitest';
  import App from './App.svelte';
  import { http, HttpResponse, passthrough } from 'msw';
  import { setupServer } from 'msw/node';

  // --- Mock Server Setup ---
  const mockArticles = [
    { abstract: "Test abstract 1", headline: { main: "Test Article 1" }, pub_date: "2024-01-01T00:00:00Z", web_url: "http://example.com/1", multimedia: [], lead_paragraph: "Lead P1", news_desk: "Test", section_name: "Testing", byline: {original: "Tester"}, _id: "1" },
    { abstract: "Test abstract 2", headline: { main: "Test Article 2" }, pub_date: "2024-01-02T00:00:00Z", web_url: "http://example.com/2", multimedia: [], lead_paragraph: "Lead P2", news_desk: "Test", section_name: "Testing", byline: {original: "Tester"}, _id: "2" },
  ];

  const server = setupServer(
    // Mock the /api/articles endpoint
    http.get('/api/articles', () => {
      return HttpResponse.json({ response: { docs: mockArticles } });
    }),
    // Allow other requests (like for static assets) to pass through
    http.get('*', ({ request }) => {
        if (request.url.includes('nyt_logo.png')) return passthrough(); // Example for logo
        if (request.url.includes('nyt-logo.svg')) return passthrough(); // Example for logo
         // Add other assets if needed
    })
  );

  beforeAll(() => server.listen());
  afterEach(() => server.resetHandlers());
  afterAll(() => server.close());
  // --- End Mock Server Setup ---

  test('renders NYTimes logo', () => {
    render(App);
    // Use alt text or other accessible attributes if available
    const logo = screen.getByAltText(/NYTimes Logo/i); // Adjust selector as needed
    expect(logo).toBeInTheDocument();
  });

  test('renders header section (e.g., title or date)', () => {
    render(App);
    // Find an element unique to the header. This might need adjustment
    // depending on the actual content (e.g., specific text, role). 
    // Let's assume there's a main heading for the page title.
    const headerElement = screen.getByRole('heading', { level: 1, name: /New York Times Article Search/i }); // Adjust name/level as needed
    expect(headerElement).toBeInTheDocument();
    // If there's a date, add a test for it:
    // const dateElement = screen.getByText(/some date format/i);
    // expect(dateElement).toBeInTheDocument();
  });

  test('fetches and displays articles', async () => {
    render(App);

    // Wait for the first article title to appear
    const firstArticle = await screen.findByText('Test Article 1');
    expect(firstArticle).toBeInTheDocument();

    // Check if the second article is also rendered
    const secondArticle = screen.getByText('Test Article 2');
    expect(secondArticle).toBeInTheDocument();

    // Optional: Check for other elements within the articles if needed
    // const firstSnippet = screen.getByText(/Test abstract 1/i);
    // expect(firstSnippet).toBeInTheDocument();
  });

</script> 