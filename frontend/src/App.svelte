<script lang="ts">
  import { onMount } from "svelte";

  let today: string = "";
  let articles: any[] = [];
  let loading: boolean = true;
  let error: string = "";

  onMount(async () => {
    const options: Intl.DateTimeFormatOptions = {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    };
    today = new Date().toLocaleDateString("en-US", options);

    try {
      const res = await fetch("/api/articles");
      console.log(res);
      const data = await res.json();
      articles = data.response.docs;
      loading = false;
    } catch (error) {
      console.error("Failed to fetch articles:", error);
      error = "Failed to load articles.";
      loading = false;
    }
  });
  function getImage(article: any): string {
    if (article?.multimedia && article.multimedia.default?.url) {
      return article.multimedia.default.url;
    }
    return "";
  }
</script>

<!-- html structure -->
<main>
  <header>
    <div class="header-top">
      <div class="date-time-container">
        <div class="date">{today}</div>
        <div class="time">
          {new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })}
        </div>
      </div>
      <div class="weather">Today: Partly cloudy. High 68. Low 52.</div>
    </div>
    <div class="logo">
      <img src="/nyt_logo.png" alt="The New York Times Logo" />
    </div>
    <nav>
      <ul>
        <li><a href="#">World</a></li>
        <li><a href="#">U.S.</a></li>
        <li><a href="#">Politics</a></li>
        <li><a href="#">Business</a></li>
        <li><a href="#">Tech</a></li>
        <li><a href="#">Science</a></li>
        <li><a href="#">Health</a></li>
        <li><a href="#">Sports</a></li>
        <li><a href="#">Arts</a></li>
      </ul>
    </nav>
  </header>

  {#if loading}
    <p>Loading articles...</p>
  {:else if error}
    <p>{error}</p>
  {:else}
    <div class="container">
      <!-- First Column -->
      <section class="column">
        {#if articles[1]}
          <article class="featured">
            <a
              href={articles[1].web_url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <h2>{articles[1].headline.main}</h2>
              <p class="byline">{articles[1].byline?.original}</p>
              <p>{articles[1].snippet}</p>
              {#if getImage(articles[1])}
                <img
                  src={getImage(articles[1])}
                  alt={articles[1].headline.main}
                  class="responsive-img"
                />
              {/if}
            </a>
          </article>
        {/if}
        {#if articles[2]}
          <article>
            <h3>{articles[2].headline.main}</h3>
            <p class="byline">{articles[2].byline?.original}</p>
            <p>{articles[2].snippet}</p>
          </article>
        {/if}
      </section>

      <!-- Second Column -->
      <section class="column">
        {#if articles[0]}
          <article>
            <a
              href={articles[0].web_url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <h2>{articles[0].headline.main}</h2>
              <p class="byline">{articles[0].byline?.original}</p>
              <p>{articles[0].snippet}</p>
            </a>
          </article>
        {/if}
        {#if articles[3]}
          <article>
            <a
              href={articles[3].web_url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <h3>{articles[3].headline.main}</h3>
              <p class="byline">{articles[3].byline?.original}</p>
              {#if getImage(articles[3])}
                <img
                  src={getImage(articles[3])}
                  alt={articles[3].headline.main}
                  class="responsive-img"
                />
              {/if}
              <p>{articles[3].snippet}</p>
            </a>
          </article>
        {/if}
      </section>

      <!-- Third Column -->
      <section class="column">
        {#if articles[4]}
          <article>
            <a
              href={articles[4].web_url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <h3>{articles[4].headline.main}</h3>
              <p class="byline">{articles[4].byline?.original}</p>
              {#if getImage(articles[4])}
                <img
                  src={getImage(articles[4])}
                  alt={articles[4].headline.main}
                  class="responsive-img"
                />
              {/if}
              <p>{articles[4].snippet}</p>
            </a>
          </article>
        {/if}
        {#if articles[5]}
          <article>
            <h3>{articles[5].headline.main}</h3>
            <p class="byline">{articles[5].byline?.original}</p>
            <p>{articles[5].snippet}</p>
          </article>
        {/if}
      </section>
    </div>
  {/if}
</main>

<footer>
  <div class="footer-content">
    <div class="footer-section">
      <h4>News</h4>
      <ul>
        <li><a href="#">World</a></li>
        <li><a href="#">Politics</a></li>
        <li><a href="#">Science</a></li>
      </ul>
    </div>
    <div class="footer-section">
      <h4>More</h4>
      <ul>
        <li><a href="#">Tech</a></li>
        <li><a href="#">Business</a></li>
        <li><a href="#">Health</a></li>
      </ul>
    </div>
  </div>
  <div class="copyright">
    <p>&copy; 2025 The New York Times Company. All Rights Reserved.</p>
  </div>
</footer>