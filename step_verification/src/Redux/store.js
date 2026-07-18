import { configureStore, createSlice } from "@reduxjs/toolkit";

const formSlice = createSlice({
  name: "form",
  initialState: {
    step: 1,
    data: {
      name: "",
      email: "",
      address: "",
      
      city: ""
    },
    result:[]
  },
  reducers: {
    nextStep: (state) => { state.step += 1 },
    prevStep: (state) => { state.step -= 1 },
    updateForm: (state, action) => {
      state.data = { ...state.data, ...action.payload };
    },
    resetForm: (state) => {
      state.step = 1;
      state.result=[...state.result,state.data]
      state.data = { name: "", email: "", address: "", city: "" };
    }
  }
});

export const { nextStep, prevStep, updateForm, resetForm } = formSlice.actions;

const store = configureStore({
  reducer: { form: formSlice.reducer }
});

export default store;
