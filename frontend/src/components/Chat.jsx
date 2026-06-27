import { useState } from "react";
import api from "../services/api";
import SourceCard from "./SourceCard";

function Chat() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [sources, setSources] = useState([]);
    const [loading, setLoading] = useState(false);

    const askQuestion = async () => {

        if (!question.trim()) {
            alert("Please enter a question.");
            return;
        }

        setLoading(true);
        setAnswer("");
        setSources([]);

        try {

            const response = await api.post("/chat/", {
                question: question
            });

            setAnswer(response.data.answer);
            setSources(response.data.sources);

        }

        catch (error) {

            setAnswer(
                error.response?.data?.detail ||
                "Unable to get answer."
            );

        }

        finally {

            setLoading(false);

        }

    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter" && !e.shiftKey) {

            e.preventDefault();

            askQuestion();

        }

    };

    return (

        <section className="card">

            <h2>💬 Ask a Question</h2>

            <textarea

                rows="5"

                value={question}

                placeholder="Ask anything about the uploaded document..."

                onChange={(e) => setQuestion(e.target.value)}

                onKeyDown={handleKeyDown}

            />

            <button

                onClick={askQuestion}

                disabled={loading}

            >

                {

                    loading

                        ?

                        "Thinking..."

                        :

                        "Ask Question"

                }

            </button>

            {

                answer &&

                <div className="answer">

                    <h3>Answer</h3>

                    <p>{answer}</p>

                </div>

            }

            {

                sources.length > 0 &&

                <div className="sources">

                    <h3>Source References</h3>

                    {

                        sources.map((source, index) => (

                            <SourceCard
                                key={index}
                                source={source}
                            />

                        ))

                    }

                </div>

            }

        </section>

    );

}

export default Chat;