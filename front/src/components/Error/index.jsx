

export const Error =  (props) => {

    return(
        <div className=" fixed h-[100vh] w-[100vw] flex">
            <div className="w-full h-60px mt-[calc(50vh-30px)] mb-[calc(50vh-30px)] bg-red-500 bg-opacity-20 backdrop-blur-sm ">
                <p className="w-full text-center font-satoshi-bolditalic text-xl mt-[16px] text-slate-300">
                    {props.text}
                </p>
                
            </div>
        </div>
    )
}