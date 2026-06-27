function SourceCard({ source }) {

    return (

        <div className="source-card">

            <strong>{source.document}</strong>

            <p>Page : {source.page}</p>

            <p>Chunk : {source.chunk}</p>

        </div>

    );

}

export default SourceCard;