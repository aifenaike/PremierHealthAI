import { env } from "$env/dynamic/public";
import { io } from "socket.io-client";
import { readable } from 'svelte/store'
export const PharmacistSocket = io(`http://localhost:5000`, {autoConnect: false});

export interface TranscriptMessage{
    speaker: number | string;
    text: string;
};

export let connected = readable(false, (set)=>{
    PharmacistSocket.on('connect', ()=>{
        console.log('socketio connected')
        set(true);
    })
    PharmacistSocket.on('disconnect', ()=>{
        console.log('socketio disconnected')
        set(false);
    })
    PharmacistSocket.connect();
})