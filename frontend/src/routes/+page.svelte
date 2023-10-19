<!-- <script lang="ts">
  import { Content } from "carbon-components-svelte";
</script>

<Content>
  <h1>Welcome to PremierAI</h1>
</Content> -->


<script lang="ts">
  import { Content } from "carbon-components-svelte";
    import { Number_3 } from "carbon-icons-svelte";
</script>

<style>
  /* Add some styling for aesthetics */
  .container {
    text-align: center;
    padding: 30px;
    border-radius: 10px;
    margin: 20px;
  }

  h1 {
    padding: 20px;
    color: #f4f4f4;
    font-size: 2.5rem;
    margin-bottom: 10px;
  }

  ul {
    padding: 20px;
    list-style-type: disc;
    text-align: left;
    color: #f4f4f4;
    font-size: 1.2rem;
    line-height: 1.5;
  }

  .container p {
    padding: 20px;
    text-align: left;
    color: #f4f4f4;
    font-size: 1.2rem;
    line-height: 1.5;
  }

  .about {
    display: flex;
    flex-direction: row;
    gap: 4%;
    justify-content: center;
    justify-items: center;
    align-items: center;
  }

  img {
    width: 250px;
    height: 250px;
    padding: 10px;
  }

  section {
    /* padding: 20px; */
  }

  .about div {
    margin: 0 auto;
  }

  h2 {
    text-align: center;
    padding-bottom: 2%;
  }
 
  @media (max-width: 600px) {
  .about {
    flex-direction: column;
  }

}

</style>

<Content>
  <div class="container">
    <h1>Welcome to PremierHealth AI</h1>
    <p>Welcome to a new era of pharmaceutical excellence! We are proud to present our innovative AI solution designed to revolutionize the way pharmacists work. With our cutting-edge technology, we're making a significant impact on the pharmacy industry by providing invaluable support to pharmacists in three key areas:</p>
    <ul>
      <li><strong>Diagnosis Assistance</strong>: Our AI solution is your trusted partner in accurate and efficient diagnosis. It assists pharmacists by providing real-time insights and information, enabling them to make well-informed decisions and offer the best care to their patients.</li>
      <li><strong>Comprehensive Drug Information</strong>: Access to up-to-date information about drugs is now at your fingertips. Our AI platform empowers pharmacists with a vast database of drug details, including usage guidelines, interactions, side effects, and more, ensuring that you have the most current and reliable information available.</li>
      <li><strong>Inventory Management</strong>: Say goodbye to inventory management hassles. Our AI system simplifies and streamlines the entire process, allowing you to optimize stock levels, reduce wastage, and ensure that essential medications are always available to serve your patients.</li>
    </ul>
  </div>
  <section>
    <h2>Meet The Team</h2>
    <div class="about">
      <div>
        <img src="./Sodiq.jpg" alt="" srcset="">
        <h4>Babawale, Sodiq Damilola</h4>
        <p>Machine Learning Engineer.</p>
      </div>
      <div>
        <img src="./James.jpeg" alt="" srcset="">
        <h4>Olayinka, James Adisa</h4>
        <p>Data Engineer and Operations Analyst.</p>
      </div>
      <div>
        <img src="./Alex.jpg" alt="" srcset="">
        <h4>Ifenaike, Alexander Oluwasina</h4>
        <p>Machine Learning Engineer.</p>
      </div>
    </div>
  </section>

</Content>
