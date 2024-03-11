
export const BasicButton = (props) => {

    return (
        <div className=" p-[2px] rounded-md bg-gradient-to-r from-blue-500 to-echo inline-block" >
            <button className="py-1 px-2 rounded-md bg-slate-800 text-blue-300">
            {props.text}
            </button>
        </div>
        
    )
}