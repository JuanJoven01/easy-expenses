
export const FormButton = (props) => {

    function handleClick(event) {
        event.preventDefault();
      }

    return (
        <div >
            <button onClick={handleClick} className="py-1 px-2 rounded-md bg-slate-800 text-blue-300 border-[2px] border-slate-500">
            {props.text}
            </button>
        </div>
        
    )
}