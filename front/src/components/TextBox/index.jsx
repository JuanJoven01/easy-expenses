

export const TextBox = (props) => {

    return (

        <p className=" mx-auto font-satoshi-mediumitalic text-center p-10 text-slate-300 bg-radial-gradient from-gradient_alpha via-gradient_bravo to-transparent to-70% backdrop-blur-sm">
            {props.text}
        </p>
    )
}