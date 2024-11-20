import streamlit as st

data = '''
- Having Tailwind, you have to write long  className which might  not be comfortable to most of the developers 
```
className = "w-full max-w-sm p-8 mx-auto rounded shadow-md bg-gradient-to-b from-stone-700 to-stone-800"
```

- Tailwind works really well with React.js, we can make utility components with tailwind for reusability 

Input.jsx
```
export default function Input({label, invalid, ...props}) {
	let labelClasses = 'block mb-2 text-xs font-bold tracing-wide uppercase';
	let inputClasses = 'w-full px-3 py-2 leading-tight border rounded shadow';

	return (
		<p>
			<label className={labelClasses}>{label}</label>
			<input className={inputClasses} {...props} />
		</p>
	)
}
```

AuthInputs.jsx
```
import {Input} from "./..."; //import from directory

<Input
	...//your code
/>
```


# Advantages & Disadvantages

### Advantages

- You don't need to know (a lot about) CSS
- Rapid Development
- No style clashes between components since you don't define any CSS rules
- Highly configurable & extensible
- CSS code is decoupled from JSX code
- You write CSS code as you know and love it
- CSS code can be written by another developer who needs only a minimal amount of access to your JSX code

### Disadvantages

- Relatively long className values
- Any style changes require editing JSX
- You end up with many relatively small "wrapper" components OR lots of copy & pasting
- You need to know CSS
- CSS code is not scoped to components -> CSS rules may clash across components (e.g., same CSS class name used in different components for different purposes)
'''
st.markdown("### Advantages and Disadvantages of Tailwind")
st.markdown(data)