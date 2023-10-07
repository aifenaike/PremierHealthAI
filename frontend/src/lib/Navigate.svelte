<script lang="ts">
  import { page } from "$app/stores";
  import { Button, Header, HeaderNav, HeaderNavItem } from "carbon-components-svelte";
  import { PharmacistSocket, connected } from "../types";
  let isSideNavOpen = false;

  let running = false

  const stopMic = ()=>{
    PharmacistSocket.emit("stop_recording", undefined, (value: boolean)=>{
      if (value) {
        running = false
      }
    })
  }

  const startMic = ()=> {
    PharmacistSocket.emit("start_recording", undefined, (value: boolean)=>{
      if (value) {
        running = true
      }
    })
  }
</script>

<Header company="PremierHealth" platformName="AI" bind:isSideNavOpen>
  {#if $connected}
    {#if running}
    <Button on:click={stopMic} kind="danger">Stop</Button>  
    {:else}
    <Button on:click={startMic}>Start</Button>  
    {/if}
  {:else}
  <Button on:click={stopMic} disabled>Not connected</Button>  
  {/if}
  
  <HeaderNav>
    <HeaderNavItem
      isSelected={$page.url.pathname === "/pharmacist" ? true : false}
      href="/pharmacist"
      text="Diagnosis Assistant"
    />
    <HeaderNavItem
      isSelected={$page.url.pathname === "/assistant" ? true : false}
      href="/assistant"
      text="AI Assistant"
    />
  </HeaderNav>
</Header>
