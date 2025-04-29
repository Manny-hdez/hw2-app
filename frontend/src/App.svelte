<script lang="ts">
  import { onMount } from "svelte";

  let today: string = "";
  let articles: any[] = [];
  let loading: boolean = true;
  let error: string = "";

  onMount(async () => {
    today = new Date().toLocaleDateString();

    try {
      const res = await fetch("/api/articles");
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
  <div class="logo-container">
    <div class="header">
      <div class="date-container">
        <p>
          <span class="date">{today}</span><br />
          <span class="place">Today's Paper</span>
        </p>
      </div>
      <div class="logo">
        <img src="/nyt_logo.png" alt="The New York Times Logo" />
      </div>
    </div>
  </div>
  <hr />

  {#if loading}
    <p>Loading articles...</p>
  {:else if error}
    <p>{error}</p>
  {:else}
    <div class="grid-container">
      <!-- ==================== Left Column ==================== -->
      <div class="left-column">
        {#if articles.length > 1}
          {#if getImage(articles[1])}
            <img src={getImage(articles[1])} alt={articles[1].headline.main} />
          {/if}
          <h2>{articles[1].headline.main}</h2>
          <p>{articles[1].snippet}</p>
          <br />
          <hr />
        {/if}

        {#if articles.length > 2}
          <h2>{articles[2].headline.main}</h2>
          <p>{articles[2].snippet}</p>
          <br />
          <hr />
        {/if}
      </div>

      <!-- ==================== Middle Column ==================== -->
      <div class="middle-column">
        {#if articles.length > 0}
          <h1>{articles[0].headline.main}</h1>
          <p>{articles[0].lead_paragraph}</p>
          <br />
          <hr />
          <br />
          {#if articles.length > 3}
            {#if getImage(articles[3])}
              <img
                src={getImage(articles[3])}
                alt={articles[3].headline.main}
              />
            {/if}
            <h3>{articles[3].headline.main}</h3>
            <p>{articles[3].snippet}</p>
          {/if}
        {/if}
      </div>

      <!-- ==================== Right Column ==================== -->
      <div class="right-column">
        {#if articles.length > 4}
          {#if getImage(articles[4])}
            <img src={getImage(articles[4])} alt={articles[4].headline.main} />
          {/if}
          <h2>{articles[4].headline.main}</h2>
          <p>{articles[4].snippet}</p>
          <br />
          <hr />
        {/if}

        {#if articles.length > 5}
          <h2>{articles[5].headline.main}</h2>
          <p>{articles[5].snippet}</p>
        {/if}
      </div>
    </div>
  {/if}

  <hr style="height: 2px; background-color: black; margin: 2% 2% 3% 2%" />
</main>