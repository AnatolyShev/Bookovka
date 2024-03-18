import {makeAutoObservable} from "mobx";

export default class UserStore{
    constructor() {
        this._isUser = {}
        this._isAuth = false
        this._isSuperRole = {}

        makeAutoObservable(this)
    }
    setIsUser(bool){
        this._isUser = bool
    }

    setIsAuth(bool){
        this._isAuth = bool
    }

    setUser(bool){
        this._isSuperRole = bool
    }


    get isAuth() {
        return this._isAuth
    }
    get isUser(){
        return this._isUser
    }
    get isSuperRole(){
        return this._isSuperRole
    }
}