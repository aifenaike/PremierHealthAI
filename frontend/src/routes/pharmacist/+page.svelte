<script lang="ts">
  import Diagnosis from "$lib/Diagnosis.svelte";
  import Report from "$lib/Report.svelte";
  import Conversation from "../../lib/Conversation.svelte";

  
</script>

<div class="flex justify-around gap-x-2 h-[90vh] mx-5">
  <div class="w-2/3 h-full flex flex-col gap-y-3">
    <div class="h-2/3">
      <Conversation />
    </div>
    <div class="h-2/3">
      <Diagnosis />
    </div>
  </div>
  <div class="w-1/3 h-full">
    <Report />
  </div>
</div>
