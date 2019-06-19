export class HttpUtils {
    static get = (aUrl, aCallback) => {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = () => { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}