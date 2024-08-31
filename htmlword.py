def setting(time,ip,port):
    return '''<!DOCTYPE html>

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

<title>PRCS安全警告</title>

<style type="text/css">

body,div,h3,h4,li,ol{margin:0;padding:0}

body{font:14px/1.5 'Microsoft YaHei','微软雅黑',Helvetica,Sans-serif;min-width:1200px;background:#f0f1f3;}

:focus{outline:0}

h3,h4,strong{font-weight:700}

a{color:#428bca;text-decoration:none}

a:hover{text-decoration:underline}

.error-page{background:#f0f1f3;padding:80px 0 180px}

.error-page-container{position:relative;z-index:1}

.error-page-main{position:relative;background:#f9f9f9;margin:0 auto;width:617px;-ms-box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:50px 50px 70px}

.error-page-main:before{content:'';display:block;background:url(img/errorPageBorder.png?1427783409637);height:7px;position:absolute;top:-7px;width:100%;left:0}

.error-page-main h3{font-size:24px;font-weight:400;border-bottom:1px solid #d0d0d0}

.error-page-main h3 strong{font-size:54px;font-weight:400;margin-right:20px}

.error-page-main h4{font-size:20px;font-weight:400;color:#333}

.error-page-actions{font-size:0;z-index:100}

.error-page-actions div{font-size:14px;display:inline-block;padding:30px 0 0 10px;width:50%;-ms-box-sizing:border-box;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;color:#838383}

.error-page-actions ol{list-style:decimal;padding-left:20px}

.error-page-actions li{line-height:2.5em}

.error-page-actions:before{content:'';display:block;position:absolute;z-index:-1;bottom:17px;left:50px;width:200px;height:10px;-moz-box-shadow:4px 5px 31px 11px #999;-webkit-box-shadow:4px 5px 31px 11px #999;box-shadow:4px 5px 31px 11px #999;-moz-transform:rotate(-4deg);-webkit-transform:rotate(-4deg);-ms-transform:rotate(-4deg);-o-transform:rotate(-4deg);transform:rotate(-4deg)}

.error-page-actions:after{content:'';display:block;position:absolute;z-index:-1;bottom:17px;right:50px;width:200px;height:10px;-moz-box-shadow:4px 5px 31px 11px #999;-webkit-box-shadow:4px 5px 31px 11px #999;box-shadow:4px 5px 31px 11px #999;-moz-transform:rotate(4deg);-webkit-transform:rotate(4deg);-ms-transform:rotate(4deg);-o-transform:rotate(4deg);transform:rotate(4deg)}

</style>

</head>

<body>

<div class="error-page">

    <div class="error-page-container">

        <div class="error-page-main">

            <h3>

                <img src='https://www.potatocraft.top/PotatoRiskControlSystem/icon/icon.png'><strong>Error</strong>无法连接！

            </h3>

            <div class="error-page-actions">
'''+F'''
                <div>
                    <h4>无法连接至:</h4>

                        <li>{ip}:{port}</li>


                    <h4>注意！</h4>

                    <ol>

                        <li>服务器在{time}时发生了崩溃!</li>

                        <li>无法连接至服务器，请及时检查!!!</li>

                    </ol>
                    <h4>----------------------------</h4>

                        <li>此服务由<a href="https://www.potatocraft.top/PotatoRiskControlSystem">Potatocraft</a>提供</li>

                </div>

            </div>

        </div>

    </div>

</div>

</body>

</html>
'''