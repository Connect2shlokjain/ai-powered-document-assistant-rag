import { useEffect, useState } from "react";
import api from "../services/api";

function History() {

    const [history, setHistory] = useState([]);
    const [loading, setLoading] = useState(true);

    const fetchHistory = async () => {

        try {

            const response = await api.get("/history/");

            setHistory(response.data);

        }

        catch (error) {

            console.error("Unable to load history.", error);

        }

        finally {

            setLoading(false);

        }

    };

    const clearHistory = async () => {

        try {

            await api.delete("/history/");

            setHistory([]);

        }

        catch (error) {

            console.error("Unable to clear history.", error);

        }

    };

    useEffect(() => {

        fetchHistory();

    }, []);

    return (

        <section className="card">

            <div className="history-header">

                <h2>🕒 Chat History</h2>

                <button onClick={clearHistory}>

                    Clear History

                </button>

            </div>

            {

                loading ?

                    <p>Loading history...</p>

                    :

                    history.length === 0 ?

                        <p>No conversations yet.</p>

                        :

                        history.map((item, index) => (

                            <div
                                className="history-card"
                                key={item.id || index}
                            >

                                <h4>Question</h4>

                                <p>{item.question}</p>

                                <br />

                                <h4>Answer</h4>

                                <p>{item.answer}</p>

                            </div>

                        ))

            }

        </section>

    );

}

export default History;