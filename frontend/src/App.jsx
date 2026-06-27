import Header from "./components/Header";
import Upload from "./components/Upload";
import Chat from "./components/Chat";
import History from "./components/History";

import "./App.css";

function App() {

    return (

        <div className="container">

            <Header />

            <Upload />

            <Chat />

            <History />

            <footer>

                Built with ❤️ using FastAPI • React • ChromaDB • Groq

            </footer>

        </div>

    );

}

export default App;