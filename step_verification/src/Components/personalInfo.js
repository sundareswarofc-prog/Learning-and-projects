import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateForm, nextStep } from "../Redux/store";

function PersonalInfo() {
  const dispatch = useDispatch();
  const data=useSelector((state) => state.form.result);
  console.log('data', data)
  const { name, email } = useSelector((state) => state.form.data);


  const handleChange = (e) => {
    dispatch(updateForm({ [e.target.name]: e.target.value }));
  };

  return (
    <div>
      <h2>Step 1: Personal Info</h2>
      <input name="name" value={name} onChange={handleChange} placeholder="Name" />
      <input name="email" value={email} onChange={handleChange} placeholder="Email" />
      <button onClick={() => dispatch(nextStep())}>Next</button>

      <div>
        {
          data.map((data)=>{
            return (
              <div>
                {data.name}
              </div>
            )
          })
        }
      </div>
    </div>
  );
}

export default PersonalInfo;
