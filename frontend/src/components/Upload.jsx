import { useState } from "react";
import api from "../services/api";

function Upload() {

    const [file, setFile] = useState(null);

    const [message, setMessage] = useState("");

    const [loading, setLoading] = useState(false);

    const uploadDocument = async () => {

        if (!file) {

            alert("Please select a document.");

            return;

        }

        setLoading(true);

        setMessage("");

        const formData = new FormData();

        formData.append("file", file);

        try {

            const response = await api.post(
                "/upload/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            setMessage(
                `✅ ${response.data.filename} uploaded successfully`
            );

        }

        catch (error) {

            setMessage(

                error.response?.data?.detail ||

                "Upload failed."

            );

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <section className="card">

            <h2>📂 Upload Document</h2>

            <input

                type="file"

                accept=".pdf,.docx,.txt"

                onChange={(e) => setFile(e.target.files[0])}

            />

            <button

                onClick={uploadDocument}

                disabled={loading}

            >

                {

                    loading

                        ?

                        "Uploading..."

                        :

                        "Upload"

                }

            </button>

            <p>

                {message}

            </p>

        </section>

    );

}

export default Upload;