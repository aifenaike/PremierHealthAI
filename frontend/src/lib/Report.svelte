<script lang="ts">
  import { Tile, TextArea, Button, ButtonSet } from "carbon-components-svelte";
  import ArrowRight from "carbon-icons-svelte/lib/ArrowRight.svelte";
  import DiagramReference from "carbon-icons-svelte/lib/DiagramReference.svelte";
  import { onMount } from "svelte";
  import { PharmacistSocket } from "../types";

  let value = ``;

  onMount(() => {

    PharmacistSocket.on("generate_notes", (x) => {
      console.log(x);
      value = x
    });
  });

  const generate = () => {
    PharmacistSocket.emit("generate_notes", value);
  };

  const setSummary = () => {
    PharmacistSocket.emit("set_summary", value)
  };

</script>

<div class="w-full flex flex-col justify-start">
  <Tile class="block">
    <p class="text-lg">Diagnosis Report</p>
  </Tile>
  <TextArea
    hideLabel
    placeholder={`Record any details not captured in the transcript here. You can then use "Diagnose" to autogenerate a full diagnosis summary.`}
    class="mt-2 block"
    bind:value
    on:change={setSummary}
    rows={30}
  />
  <ButtonSet class="flex justify-end mt-2">
    <!-- <Button
      on:click={() => {
        location.reload();
      }}
      kind="danger-ghost">Reset</Button
    > -->
    <Button icon={DiagramReference} class="block" kind="secondary" on:click={generate}
      >Diagnose</Button
    >
  </ButtonSet>

  <div />
</div>
