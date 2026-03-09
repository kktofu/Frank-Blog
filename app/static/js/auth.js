function refreshToken(){

    const refresh = localStorage.getItem("refresh")

    return fetch("/api/token/refresh/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            refresh: refresh
        })
    })
    .then(res => {

        if(!res.ok){
            throw new Error("refresh failed")
        }

        return res.json()

    })
    .then(data => {

        localStorage.setItem("access", data.access)

        return data.access
    })
}

function authenticatedFetch(url, options = {}){

    const token = localStorage.getItem("access")

    options.headers = {
        ...options.headers,
        "Authorization": `Bearer ${token}`
    }

    return fetch(url, options)
    .then(res => {

        if(res.status === 401){

            return refreshToken()
            .then(newToken => {

                options.headers["Authorization"] = `Bearer ${newToken}`

                return fetch(url, options)

            })

        }

        return res

    })
}