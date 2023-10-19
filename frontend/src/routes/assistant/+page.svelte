<script lang="ts">
  import {
    TextInput,
    Button,
    Tile,
    Form,
    TextInputSkeleton,
  } from "carbon-components-svelte";
  import SendFilled from "carbon-icons-svelte/lib/SendFilled.svelte";
  import Monster from "carbon-icons-svelte/lib/Monster.svelte";
  import { PharmacistSocket } from "../../types";
  import { onDestroy } from "svelte";
  import { MicrophoneFilled } from "carbon-icons-svelte";

  let value = "";
  let streamingMedia = false;

  let x: {
    message?: string;
    type: "pharmacist" | "bot";
    audio?: HTMLAudioElement;
  }[] = [
    {
      message:
        "Hello I'm PremierHealthAI bot, your personal knowledge assistant ask me any questions about a specific drug and medication",
      type: "bot",
    },
  ];
  PharmacistSocket.emit("patient_mode", true);

  interface IContent {
    text: string;
    done: boolean;
  }

  PharmacistSocket.on("patient_message", (content: IContent) => {
    console.log(content);
    if (x[x.length - 1].type === "bot") {
      x = [...x.slice(0, x.length - 1), { message: content.text, type: "bot" }];
    } else {
      x = [...x, { message: content.text, type: "bot" }];
    }

    if (content.done) {
      x = [
        ...x.slice(0, x.length - 1),
        { message: content.text, type: "bot"},
      ];
      if (value){
        postMessage()
      }
    }
  });

  PharmacistSocket.on("patient_transcript", (text) => {
    value = text + value
    if (!streamingMedia) {
      postMessage()
    }
    streamingMedia = true
  });


  const postMessage = () => {
    x = [...x, { message: value, type: "pharmacist" }];
    PharmacistSocket.emit("patient_message", value);
    value = "";
  };

  let recording = false;

  const toggleRecording = () => {
    if (recording) {
      recording = false;
      PharmacistSocket.emit("patient_recording", false);
    } else {
      recording = true;
      PharmacistSocket.emit("patient_recording", true);
    }
  };

  onDestroy(() => {
    PharmacistSocket.emit("patient_mode", false);
  });
</script>

<div class="h-[93vh] flex flex-col bg-repeat bg-x relative">
  <div class="flex flex-col gap-y-3 mb-22 lg:w-[60%] mx-auto">
    {#each x as y}
      <div
        class="flex {y.type === 'pharmacist' ? 'flex-row-reverse' : 'flex-row'}"
      >
        {#if y.type !== "pharmacist"}
          <div class="rounded-full bg-dark-400">
            <Monster size={32} class="block m-auto" />
          </div>
        {/if}
        <Tile
          class="w-[60%] rounded-md shadow-sm {y.type === 'pharmacist'
            ? 'ml-auto'
            : 'mr-auto'}"
        >
          {#if y.audio}
            <audio controls src={y.audio.src} />
          {/if}
          {#if y.message}
            <p>{y.message}</p>
          {/if}
        </Tile>
      </div>
    {/each}
  </div>

  <div class="flex absolute bottom-1 w-full px-6 py-3 bg-dark-600">
    <Button
      type="submit"
      on:click={toggleRecording}
      kind={recording ? "danger" : "ghost"}
      icon={MicrophoneFilled}
      size="xl"
    />
    <Form on:submit={postMessage} class=" w-full flex">
      {#if !streamingMedia}
        <TextInput
          size="xl"
          hideLabel
          labelText="User name"
          placeholder="Ask your questions here"
          bind:value
          autofocus
        />
      {:else}
        <TextInputSkeleton hideLabel />
      {/if}
      <Button type="submit" kind="ghost" icon={SendFilled} size="xl" />
    </Form>
  </div>
</div>

<style>
  .bg-x {
    /* background-image: url("/pharm_bg2.jpg"); */
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-attachment: fixed; /* Optional, it keeps the background fixed while scrolling */
    background-position: center center; /* Optional, it centers the background image */
  }
</style>