import React, {useContext, useEffect, useState} from 'react';
import {BrowserRouter} from "react-router-dom";
import AppRouter from "./components/AppRouter";
import NavBar from "./components/NavBar";
import {observer} from "mobx-react-lite";
import {Context} from "./index";
import {check} from "./http/userAPI";
import {Spinner} from "react-bootstrap";
// import 'react-toastify/dist/ReactToastify.css';

const App = observer(() => {
    const {user} = useContext(Context)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        check()
            .then(data => {
                if (data && data.role && data.id) {
                    user.setUser(data.role);
                    user.setIsUser(data.id);
                    user.setIsAuth(true);
                }
            })
            .finally(() => setLoading(false));
    }, []);

    return (
        <BrowserRouter>
            <NavBar />
            <AppRouter />
        </BrowserRouter>
    );
});

export default App;
