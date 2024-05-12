import { useState } from "react";

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <div className="flex flex-col items-center h-screen">
                <div className="flex justify-center navbar bg-base-100">
                    <a className="btn btn-ghost text-xl">
                        Youtube Playlist Downloader
                    </a>
                </div>

                <input
                    type="text"
                    placeholder="Paste the playlist url here..."
                    className="input input-bordered input-primary w-full max-w-xs mt-48"
                />

                <button className="btn btn-primary mt-5">Download</button>

                <a className="link link-primary absolute bottom-1" href="#">github repo link</a>
            </div>
        </>
    );
}

export default App;
