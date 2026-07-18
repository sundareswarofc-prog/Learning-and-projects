import { useEffect, useState } from "react";

const useFetchApiHook = (url) => {
    const [data, setData] = useState(0);
    const [loading, setLoading] = useState(true);
    const[error,setError]=useState('')

    useEffect(() => {
        const fetchdata = async () => {
            try {
                const response = await fetch(url, {
                    method: "get",
                })
                const data = await response.json();
                setData(data)
            }
            catch (err) {
                console.log(err)
                setError(err.message)
            }
            finally{
                setLoading(false)
            }
        }
       fetchdata()  
    }, [url])
    return {data,loading,error};
}

export default useFetchApiHook;