<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1UdRycuunGeBiQZGSa7vClz3GrLgZCkRn#scrollTo=QWEJysFJvmcq -->
<html lang="en" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" charset="utf-8" src="./day3_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-N1PkUIetmAew8IlwnkjTZKCfj/8qzxyh0nDsYbSE2HroblBEtmK3+xAW3hJDJD3h" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./day3_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-N1PkUIetmAew8IlwnkjTZKCfj/8qzxyh0nDsYbSE2HroblBEtmK3+xAW3hJDJD3h" nonce=""></script><script src="./day3_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./day3_files/cb=gapi.loaded_0" nonce="" async=""></script><script type="text/javascript" async="" src="./day3_files/js" nonce=""></script><script async="" src="./day3_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Untitled1.ipynb - Colab</title><link href="./day3_files/css2" rel="stylesheet"><link href="./day3_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_2d:not(.gb_pe){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Pa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Pa:hover::after,a.gb_Pa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Pa:hover,a.gb_Pa:focus{text-decoration:none}a.gb_Pa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Qa{background-color:#4285f4;color:#fff}a.gb_Qa:active{background-color:#0043b2}.gb_Ra{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Pa,.gb_Qa,.gb_Sa,.gb_Ta{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Sa{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ta{background:#f8f8f8}.gb_Sa,#gb a.gb_Sa.gb_Sa,.gb_Ta{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ta{cursor:default;text-decoration:none}.gb_Ta{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ta{color:#fff}.gb_Ta:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ta:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Ua{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Ua:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Ua:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Ua:active,#gb .gb_Ua:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Ua.gb_F{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Ua.gb_F:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Ua.gb_F:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Ua.gb_F:active,#gb .gb_Ua.gb_F:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_bd{display:inline-block;vertical-align:middle}.gb_Oe .gb_P{bottom:-3px;right:-5px}.gb_C{position:relative}.gb_A{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_A{cursor:pointer;text-decoration:none}.gb_A,a.gb_A{color:#000}.gb_cd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_dd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_dd{border-bottom-color:#ccc}.gb_ka{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_bd.gb_Sc .gb_cd,.gb_bd.gb_Sc .gb_dd,.gb_bd.gb_Sc .gb_ka,.gb_Sc.gb_ka{display:block}.gb_bd.gb_Sc.gb_ed .gb_cd,.gb_bd.gb_Sc.gb_ed .gb_dd{display:none}.gb_Pe{position:absolute;right:8px;top:62px;z-index:-1}.gb_fd .gb_cd,.gb_fd .gb_dd,.gb_fd .gb_ka{margin-top:-10px}.gb_bd:first-child,#gbsfw:first-child+.gb_bd{padding-left:4px}.gb_Ea.gb_Qe .gb_bd:first-child{padding-left:0}.gb_Re{position:relative}.gb_1c .gb_Re,.gb_Id .gb_Re{float:right}.gb_A{padding:8px;cursor:pointer}.gb_A::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Ea .gb_gd:not(.gb_Pa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_hd button svg,.gb_A{-webkit-border-radius:50%;border-radius:50%}.gb_hd button:focus:not(:focus-visible) svg,.gb_hd button:hover svg,.gb_hd button:active svg,.gb_A:focus:not(:focus-visible),.gb_A:hover,.gb_A:active,.gb_A[aria-expanded=true]{outline:none}.gb_Kc .gb_hd.gb_id button:focus-visible svg,.gb_hd button:focus-visible svg,.gb_A:focus-visible{outline:1px solid #202124}.gb_Kc .gb_hd button:focus-visible svg,.gb_Kc .gb_A:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Kc .gb_hd.gb_id button:focus-visible svg,.gb_hd button:focus-visible svg,.gb_Kc .gb_hd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Kc .gb_hd.gb_id button:focus svg,.gb_Kc .gb_hd.gb_id button:focus:hover svg,.gb_hd button:focus svg,.gb_hd button:focus:hover svg,.gb_A:focus,.gb_A:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Kc .gb_hd.gb_id button:active svg,.gb_hd button:active svg,.gb_A:active{background-color:rgba(60,64,67,.12)}.gb_Kc .gb_hd.gb_id button:hover svg,.gb_hd button:hover svg,.gb_A:hover{background-color:rgba(60,64,67,.08)}.gb_Va .gb_A.gb_Xa:hover{background-color:transparent}.gb_A[aria-expanded=true],.gb_A:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_A[aria-expanded=true] .gb_E{fill:#5f6368;opacity:1}.gb_Kc .gb_hd button:hover svg,.gb_Kc .gb_A:hover{background-color:rgba(232,234,237,.08)}.gb_Kc .gb_hd button:focus svg,.gb_Kc .gb_hd button:focus:hover svg,.gb_Kc .gb_A:focus,.gb_Kc .gb_A:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Kc .gb_hd button:active svg,.gb_Kc .gb_A:active{background-color:rgba(232,234,237,.12)}.gb_Kc .gb_A[aria-expanded=true],.gb_Kc .gb_A:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Kc .gb_A[aria-expanded=true] .gb_E{fill:#fff;opacity:1}.gb_bd{padding:4px}.gb_Ea.gb_Qe .gb_bd{padding:4px 2px}.gb_Ea.gb_Qe .gb_y.gb_bd{padding-left:6px}.gb_ka{z-index:991;line-height:normal}.gb_ka.gb_jd{left:0;right:auto}@media (max-width:350px){.gb_ka.gb_jd{left:0}}.gb_Se .gb_ka{top:56px}.gb_Q{display:none!important}.gb_md{visibility:hidden}.gb_I .gb_A,.gb_ja .gb_I .gb_A{background-position:-64px -29px}.gb_0 .gb_I .gb_A{background-position:-29px -29px;opacity:1}.gb_I .gb_A,.gb_I .gb_A:hover,.gb_I .gb_A:focus{opacity:1}.gb_K{display:none}@media screen and (max-width:319px){.gb_kd:not(.gb_ld) .gb_I{display:none;visibility:hidden}}.gb_P{display:none}.gb_8c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_8c.gb_9c{color:#3c4043}.gb_Ea.gb_bc .gb_8c{margin-bottom:0}.gb_rd.gb_td .gb_8c{padding-left:4px}.gb_Ea.gb_bc .gb_ud{position:relative;top:-2px}.gb_ad{display:none}.gb_Ea{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Ea.gb_Rc{min-width:120px}.gb_Ea.gb_vd .gb_wd{display:none}.gb_Ea.gb_vd .gb_kd{height:56px}header.gb_Ea{display:block}.gb_Ea svg{fill:currentColor}.gb_Cd{position:fixed;top:0;width:100%}.gb_xd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Dd{height:64px}.gb_kd{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ea:not(.gb_bc) .gb_kd{padding:8px}.gb_Ea.gb_Ed .gb_kd{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Ea .gb_kd.gb_ld.gb_Fd{min-width:0}.gb_Ea.gb_bc .gb_kd{padding:4px;padding-left:8px;min-width:0}.gb_wd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_zd>.gb_wd{display:table-cell;width:100%}.gb_rd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Ea.gb_bc .gb_rd{padding-right:14px}.gb_Ad{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Ad>:only-child{display:inline-block}.gb_Bd.gb_2c{padding-left:4px}.gb_Bd.gb_Hd,.gb_Ea.gb_Ed .gb_Bd,.gb_Ea.gb_bc:not(.gb_Id) .gb_Bd{padding-left:0}.gb_Ea.gb_bc .gb_Bd.gb_Hd{padding-right:0}.gb_Ea.gb_bc .gb_Bd.gb_Hd .gb_Va{margin-left:10px}.gb_2c{display:inline}.gb_Ea.gb_Vc .gb_Bd.gb_Jd,.gb_Ea.gb_Id .gb_Bd.gb_Jd{padding-left:2px}.gb_8c{display:inline-block}.gb_Bd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Id{height:48px}.gb_Ea.gb_Id{min-width:auto}.gb_Id .gb_Bd{float:right;padding-left:32px}.gb_Id .gb_Bd.gb_Kd{padding-left:0}.gb_Ld{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_od{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Md{color:black}.gb_Kc{color:white}.gb_Ea a,.gb_Oc a{color:inherit}.gb_aa{color:rgba(0,0,0,.87)}.gb_Ea svg,.gb_Oc svg,.gb_rd .gb_sd,.gb_1c .gb_sd{color:#5f6368;opacity:1}.gb_Kc svg,.gb_Oc.gb_Tc svg,.gb_Kc .gb_rd .gb_sd,.gb_Kc .gb_rd .gb_Jc,.gb_Kc .gb_rd .gb_ud,.gb_Oc.gb_Tc .gb_sd{color:rgba(255,255,255,.87)}.gb_Kc .gb_rd .gb_Nd:not(.gb_Od){opacity:.87}.gb_9c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Kc .gb_9c,.gb_Md .gb_9c{opacity:1}.gb_Pd{position:relative}.gb_L{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_W,span.gb_W{color:rgba(0,0,0,.87);text-decoration:none}.gb_Kc a.gb_W,.gb_Kc span.gb_W{color:white}a.gb_W:focus{outline-offset:2px}a.gb_W:hover{text-decoration:underline}.gb_X{display:inline-block;padding-left:15px}.gb_X .gb_W{display:inline-block;line-height:24px;vertical-align:middle}.gb_pd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Ea.gb_Id .gb_pd{margin-left:8px}#gb a.gb_Ta.gb_pd{cursor:pointer}.gb_Ta.gb_pd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ta.gb_pd:focus,.gb_Ta.gb_pd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ta.gb_pd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_pd{background:#1a73e8;border:1px solid transparent}.gb_Ea.gb_bc .gb_pd{padding:9px 15px;min-width:80px}.gb_Qd{text-align:left}#gb .gb_Kc a.gb_pd:not(.gb_F),#gb.gb_Kc a.gb_pd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ta.gb_F.gb_pd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Kc a.gb_pd:hover:not(.gb_F),#gb.gb_Kc a.gb_pd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ta.gb_F.gb_pd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Kc a.gb_pd:focus:not(.gb_F),#gb .gb_Kc a.gb_pd:focus:hover:not(.gb_F),#gb.gb_Kc a.gb_pd:focus:not(.gb_F),#gb.gb_Kc a.gb_pd:focus:hover:not(.gb_F){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ta.gb_F.gb_pd:focus,#gb a.gb_Ta.gb_F.gb_pd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Kc a.gb_pd:active:not(.gb_F),#gb.gb_Kc a.gb_pd:active{background:#ecf3fe}#gb a.gb_Ta.gb_F.gb_pd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_J{display:none}@media screen and (max-width:319px){.gb_kd .gb_I{display:none;visibility:hidden}}.gb_Va{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Va.gb_F{background-color:transparent;border:1px solid #5f6368}.gb_2a{display:inherit}.gb_Va.gb_F .gb_2a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Va:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Va.gb_F:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Va:focus-visible,.gb_Va:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Va.gb_F:focus-visible,.gb_Va.gb_F:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Va.gb_F:active,.gb_Va.gb_Sc.gb_F:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_3a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Va.gb_F .gb_3a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_3a.gb_4a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_3a.gb_4a .gb_Hc{vertical-align:middle}.gb_Ea:not(.gb_bc) .gb_Va{margin-left:10px;margin-right:4px}.gb_Rd{max-height:32px;width:78px}.gb_Va.gb_F .gb_Rd{max-height:26px;width:72px}.gb_O{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_db{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_db.gb_O{height:30px;width:30px}.gb_db.gb_O:hover,.gb_db.gb_O:active{-webkit-box-shadow:none;box-shadow:none}.gb_eb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_vc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_O::before,.gb_fb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_2 .gb_fb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_O:hover,.gb_O:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_O:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_O:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_gb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_A.gb_gb{width:auto}.gb_gb:hover,.gb_gb:focus{opacity:.85}.gb_fd .gb_gb,.gb_fd .gb_Ud{line-height:26px}#gb#gb.gb_fd a.gb_gb,.gb_fd .gb_Ud{font-size:11px;height:auto}.gb_hb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Xa:hover .gb_hb{opacity:.85}.gb_Va>.gb_y{padding:3px 3px 3px 4px}.gb_Vd.gb_md{color:#fff}.gb_0 .gb_gb,.gb_0 .gb_hb{opacity:1}#gb#gb.gb_0.gb_0 a.gb_gb,#gb#gb .gb_0.gb_0 a.gb_gb{color:#fff}.gb_0.gb_0 .gb_hb{border-top-color:#fff;opacity:1}.gb_ja .gb_O:hover,.gb_0 .gb_O:hover,.gb_ja .gb_O:focus,.gb_0 .gb_O:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Wd .gb_y,.gb_Xd .gb_y{position:absolute;right:1px}.gb_y.gb_Z,.gb_ib.gb_Z,.gb_Xa.gb_Z{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_Zd.gb_0d .gb_gb{width:30px!important}.gb_1d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_2d .gb_1d,.gb_3d .gb_1d{right:0;top:0}.gb_y .gb_A{padding:4px}.gb_R{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.rX6uZdQxZxU.2019.O","co.in","en-GB","425",0,[4,2,"","","","712356711","0"],null,"IiN-Z9fGL9yEp84Pj7CZ2A4",null,0,"og.qtm.CEsjJf2wziM.L.W.O","AA2YrTvH0Rknr6hXqx-tgqAUuIv05wLZhQ","AA2YrTvDtorsWuiBHYzP5-lS7pwgoAa95g","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","sreeharshithavakkantham246@gmail.com","","AJP8KkWBkS5t6sqC9I4UpKQSzgR0UWhR1tHzZ0E2B8LURcHKlQ4dsHKuu9sHZA8Itrnhl8zPDKnWoSOMcG3lZ2WpYbU6PzGEtw",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.ZpMpph_5a4M.O/d=1/rs=AHpOoo_c5__TAiALeuHoQOKG0BnSpdbJrQ/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20241202.0_p1","en-GB",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en-GB","712356711.0",8,null,1,0,null,null,null,null,"",null,null,null,"IiN-Z9fGL9yEp84Pj7CZ2A4",0,0,0,null,2,5,"nn",49,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.rX6uZdQxZxU.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTvH0Rknr6hXqx-tgqAUuIv05wLZhQ"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.CEsjJf2wziM.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTvDtorsWuiBHYzP5-lS7pwgoAa95g"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",1,1],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en-GB",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026timeStmp=1736319778\u0026secTok=.AG5fkS-FwnZyqWeFPIrdsJfr7uxUIQcT8g\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,1,null,0,null,0],0,null,null,null,1],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ca,ja,ka,oa,qa,ra,Ba,Ca,Fa,Ga,Ha,Qa,$a,Za,cb,eb,db,fb,gb,jb,kb,ob,rb,lb,qb,pb,nb,mb,sb,vb,Cb,Gb,Hb,Ib,Jb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Ij=!0;return a};ca=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};
_.da=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ea=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};ja=function(a){return fa?ia?ia.brands.some(({brand:b})=>b&&b.indexOf(a)!=-1):!1:!1};_.u=function(a){return _.ea().indexOf(a)!=-1};ka=function(){return fa?!!ia&&ia.brands.length>0:!1};_.la=function(){return ka()?!1:_.u("Opera")};_.ma=function(){return ka()?!1:_.u("Trident")||_.u("MSIE")};_.na=function(){return _.u("Firefox")||_.u("FxiOS")};
_.pa=function(){return _.u("Safari")&&!(oa()||(ka()?0:_.u("Coast"))||_.la()||(ka()?0:_.u("Edge"))||(ka()?ja("Microsoft Edge"):_.u("Edg/"))||(ka()?ja("Opera"):_.u("OPR"))||_.na()||_.u("Silk")||_.u("Android"))};oa=function(){return ka()?ja("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(ka()?0:_.u("Edge"))||_.u("Silk")};qa=function(){return fa?!!ia&&!!ia.platform:!1};ra=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.sa=function(){return ra()||_.u("iPad")||_.u("iPod")};
_.ta=function(){return qa()?ia.platform==="macOS":_.u("Macintosh")};_.va=function(a,b){return _.ua(a,b)>=0};_.wa=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.xa=function(a){return a!=null&&a instanceof Uint8Array};_.za=function(a,b=!1,c=!1){a=c&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol();b&&ya.add(a);return a};
_.Aa=function(a){return!!((a[_.v]|0)&2)};Ba=function(a,b){b[_.v]=(a|0)&-30975};Ca=function(a,b){b[_.v]=(a|34)&-30941};_.Da=function(a){return Array.prototype.slice.call(a)};Fa=function(a){return!(!a||typeof a!=="object"||a.i!==Ea)};Ga=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};Ha=function(a){return!Array.isArray(a)||a.length?!1:(a[_.v]|0)&1?!0:!1};_.Ia=function(a){if(a&2)throw Error();};_.La=function(a){const b=_.Ja(_.Ka);return b?a[b]:void 0};
_.Na=function(){const a=Error();Ma(a,"incident");_.da(a)};_.Oa=function(a){a=Error(a);Ma(a,"warning");return a};Qa=function(a,b){if(a!=null){var c;var d=(c=Pa)!=null?c:Pa={};c=d[a]||0;c>=b||(d[a]=c+1,_.Na())}};_.Sa=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Ra(a)+"`"+a);return a};_.Ta=function(a){if(!Number.isFinite(a))throw _.Oa("enum");return a|0};_.Ua=function(a){if(typeof a!=="number")throw _.Oa("int32");if(!Number.isFinite(a))throw _.Oa("int32");return a|0};
_.Va=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Wa=function(a){return a==null||typeof a==="string"?a:void 0};_.Ya=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Fd===_.Xa)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};$a=function(a,b){return Za(b)};
Za=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "bigint":return(0,_.ab)(a)?Number(a):String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Ha(a))return}else{if(_.xa(a))return _.wa(a);if("function"==typeof _.bb&&a instanceof _.bb)return a.j()}}return a};
cb=function(a,b,c){const d=_.Da(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}(a=_.La(a))&&(d[_.Ka]=_.Da(a));return d};eb=function(a,b,c,d,e){if(a!=null){if(Array.isArray(a))a=Ha(a)?void 0:e&&(a[_.v]|0)&2?a:db(a,b,c,d!==void 0,e);else if(Ga(a)){const f={};for(let g in a)f[g]=eb(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};
db=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0,g=d?!!(f&32):void 0;d=_.Da(a);for(let h=0;h<d.length;h++)d[h]=eb(d[h],b,c,g,e);c&&((a=_.La(a))&&(d[_.Ka]=_.Da(a)),c(f,d));return d};fb=function(a){return a.Fd===_.Xa?a.toJSON():Za(a)};
gb=function(a,b,c=Ca){if(a!=null){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;if(d&2)return a;b&&(b=d===0||!!(d&32)&&!(d&64||!(d&16)));return b?(a[_.v]=(d|34)&-12293,a):db(a,gb,d&4?Ca:c,!0,!0)}a.Fd===_.Xa&&(c=a.ha,d=c[_.v],a=d&2?a:new a.constructor(_.hb(c,d,!0)));return a}};_.hb=function(a,b,c){const d=c||b&2?Ca:Ba,e=!!(b&32);a=cb(a,b,f=>gb(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.ib=function(a){const b=a.ha,c=b[_.v];return c&2?new a.constructor(_.hb(b,c,!1)):a};jb=function(a){return a};kb=function(a){return a};ob=function(a,b,c,d){return lb(a,b,c,d,mb,nb)};rb=function(a,b,c,d){return lb(a,b,c,d,pb,qb)};
lb=function(a,b,c,d,e,f){if(!c.length&&!d)return 0;var g=0;let h=0,k=0;var l=0;let n=0;for(var p=c.length-1;p>=0;p--){var r=c[p];d&&p===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)p=+q,isNaN(p)||(n+=sb(p),h++,p>g&&(g=p));l=e(l,k)+f(h,g,n);q=k;p=h;r=g;let x=n;for(let D=c.length-1;D>=0;D--){var A=c[D];if(A==null||d&&D===c.length-1&&A===d)continue;A=D-b;const H=e(A,q)+f(p,r,x);H<l&&(a=1+A,l=H);p++;q--;x+=sb(A);r=Math.max(r,A)}b=e(0,0)+f(p,r,x);b<l&&(a=0,l=b);if(d){p=h;r=g;x=n;q=k;for(const D in d)d=
+D,isNaN(d)||d>=1024||(p--,q++,x-=D.length,g=e(d,q)+f(p,r,x),g<l&&(a=1+d,l=g))}return a};qb=function(a,b,c){return c+a*3+(a>1?a-1:0)};pb=function(a,b){return(a>1?a-1:0)+(a-b)*4};nb=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};mb=function(a){return 40+4*a};sb=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
_.ub=function(a,b,c,d){var e;d=(e=d)!=null?e:0;if(a==null)e=96,c?(a=[c],e|=512):a=[],b&&(e=e&-33521665|(b&1023)<<15);else{if(!Array.isArray(a))throw Error("t");e=a[_.v]|0;var f=Object.getOwnPropertySymbols;if(f){f=f(a);for(let g=0;g<f.length;g++)if(!ya.has(f[g])){Qa(tb,5);break}}if(e&2048)throw Error("w");if(e&64)return a;d===1||d===2||(e|=64);if(c&&(e|=512,c!==a[0]))throw Error("x");a:{d=a;c=e;if(e=d.length)if(f=e-1,Ga(d[f])){c|=256;b=f-(+!!(c&512)-1);if(b>=1024)throw Error("y");e=c&-33521665|(b&
1023)<<15;break a}if(b){b=Math.max(b,e-(+!!(c&512)-1));if(b>1024)throw Error("z");e=c&-33521665|(b&1023)<<15}else e=c}}a[_.v]=e;return a};vb=function(a,b,c,d){b=d+(+!!(b&512)-1);if(!(b<0||b>=a.length||b>=c))return a[b]};
_.wb=function(a,b,c,d){const e=b>>15&1023||536870912;if(c>=e){let f,g=b;if(b&256)f=a[a.length-1];else{if(d==null)return g;f=a[e+(+!!(b&512)-1)]={};g|=256}f[c]=d;c<e&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&(a[_.v]=g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};_.yb=function(a,b,c,d){a=a.ha;let e=a[_.v];d=_.xb(a,e,c,d);b=_.Ya(d,b,e);b!==d&&b!=null&&_.wb(a,e,c,b);return b};_.zb=function(a,b){return a!=null?a:b};
Cb=function(a){var b=a.ha;b=Ab?b:db(b,fb,void 0,void 0,!1);var c=!Ab,d=(c?a.ha:b)[_.v];if(a=b.length){var e=b[a-1],f=Ga(e);f?a--:e=void 0;var g=+!!(d&512)-1,h=a-g;d=!!Bb&&!(d&512);var k,l=(k=Bb)!=null?k:kb;k=d?l(h,g,b,e):h;d=(h=d&&h!==k)?Array.prototype.slice.call(b,0,a):b;if(f||h){b:{var n=d;var p=e;var r;f=!1;if(h)for(l=Math.max(0,k+g);l<n.length;l++){var q=n[l];const D=l-g;if(!(q==null||Ha(q)||Fa(q)&&q.size===0)){var x=n[l]=void 0;((x=r)!=null?x:r={})[D]=q;f=!0}}if(p)for(let D in p)if(x=+D,isNaN(x)){let H;
((H=r)!=null?H:r={})[D]=p[D]}else if(l=p[D],Array.isArray(l)&&(Ha(l)||Fa(l)&&l.size===0)&&(l=null),l==null&&(f=!0),h&&x<k){f=!0;l=x+g;for(q=n.length;q<=l;q++)n.push(void 0);n[l]=p[x]}else if(l!=null){let H;((H=r)!=null?H:r={})[D]=l}f||(r=p);if(r)for(let D in r){p=r;break b}p=null}n=p==null?e!=null:p!==e}h&&(a=d.length);for(;a>0;a--){r=d[a-1];if(!(r==null||Ha(r)||Fa(r)&&r.size===0))break;var A=!0}if(d!==b||n||A){if(!h&&!c)d=Array.prototype.slice.call(d,0,a);else if(A||n||p)d.length=a;p&&d.push(p)}A=
d}else A=b;return A};_.Db=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.w=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Eb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Fb=function(a){for(const b in a)return!1;return!0};Gb=Object.defineProperty;
Hb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Ib=Hb(this);Jb=function(a,b){if(b)a:{var c=Ib;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Gb(c,a,{configurable:!0,writable:!0,value:b})}};
Jb("Symbol.dispose",function(a){return a?a:Symbol("b")});Jb("globalThis",function(a){return a||Ib});Jb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});var Lb,Pb;_.Kb=_.Kb||{};_.t=this||self;Lb=_.t._F_toggles||[];_.Mb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ra=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Nb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Ob="closure_uid_"+(Math.random()*1E9>>>0);Pb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Pb;return _.z.apply(null,arguments)};
_.Qb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.B=function(a,b){a=a.split(".");var c=_.t;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Ja=function(a){return a};
_.C=function(a,b){function c(){}c.prototype=b.prototype;a.W=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.zj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.C(_.aa,Error);_.aa.prototype.name="CustomError";var Rb=!!(Lb[0]&1024);var Sb;if(Lb[0]&512)Sb=Rb;else{var Tb=_.Mb("WIZ_global_data.oxN3nb"),Ub=Tb&&Tb[610401301];Sb=Ub!=null?Ub:!1}var fa=Sb;_.Vb=_.ba(a=>typeof a==="number");_.Wb=_.ba(a=>typeof a==="string");_.Xb=_.ba(a=>typeof a==="boolean");_.Yb=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var ac,Zb,bc,$b;_.ab=_.ba(a=>_.Yb?a>=Zb&&a<=$b:a[0]==="-"?ca(a,ac):ca(a,bc));ac=Number.MIN_SAFE_INTEGER.toString();Zb=_.Yb?BigInt(Number.MIN_SAFE_INTEGER):void 0;bc=Number.MAX_SAFE_INTEGER.toString();$b=_.Yb?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.cc=typeof TextDecoder!=="undefined";_.dc=typeof TextEncoder!=="undefined";_.ec=function(){return _.ea().toLowerCase().indexOf("webkit")!=-1};var ia,fc=_.t.navigator;ia=fc?fc.userAgentData||null:null;_.ua=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.gc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.hc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.ic=function(a){_.ic[" "](a);return a};_.ic[" "]=function(){};var vc;_.jc=_.la();_.kc=_.ma();_.lc=_.u("Edge");_.mc=_.u("Gecko")&&!(_.ec()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.nc=_.ec()&&!_.u("Edge");_.oc=_.ta();_.pc=qa()?ia.platform==="Windows":_.u("Windows");_.qc=qa()?ia.platform==="Android":_.u("Android");_.rc=ra();_.sc=_.u("iPad");_.tc=_.u("iPod");_.uc=_.sa();
a:{let a="";const b=function(){const c=_.ea();if(_.mc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.lc)return/Edge\/([\d\.]+)/.exec(c);if(_.kc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.nc)return/WebKit\/(\S+)/.exec(c);if(_.jc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.kc){var wc;const c=_.t.document;wc=c?c.documentMode:void 0;if(wc!=null&&wc>parseFloat(a)){vc=String(wc);break a}}vc=a}_.xc=vc;_.yc=_.na();_.zc=ra()||_.u("iPod");_.Ac=_.u("iPad");_.Bc=_.u("Android")&&!(oa()||_.na()||_.la()||_.u("Silk"));_.Cc=oa();_.Dc=_.pa()&&!_.sa();var ya,Ec,tb;ya=new Set;_.v=_.za("jas",!0,!0);Ec=_.za();_.Ka=_.za(void 0,!0);tb=_.za();var Ea,Ic;_.Xa={};Ea={};Ic=[];Ic[_.v]=55;_.Hc=Object.freeze(Ic);_.Jc=Object.freeze({});var Ma=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};var Pa=void 0;_.Kc=function(a,b){a=a.ha;return _.xb(a,a[_.v],b)};_.xb=function(a,b,c,d){if(c===-1)return null;const e=b>>15&1023||536870912;if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;return d&&b&256&&(d=a[f-1][c],d!=null)?(vb(a,b,e,c)&&Qa(Ec,4),d):vb(a,b,e,c)}};_.Lc=function(a,b,c){const d=a.ha;let e=d[_.v];_.Ia(e);_.wb(d,e,b,c);return a};_.E=function(a,b,c,d=!1){b=_.yb(a,b,c,d);if(b==null)return b;a=a.ha;d=a[_.v];if(!(d&2)){const e=_.ib(b);e!==b&&(b=e,_.wb(a,d,c,b))}return b};
_.F=function(a,b,c){c==null&&(c=void 0);return _.Lc(a,b,c)};_.G=function(a,b){a=_.Kc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.I=function(a,b){return _.Wa(_.Kc(a,b))};_.J=function(a,b,c=!1){return _.zb(_.G(a,b),c)};_.K=function(a,b){return _.zb(_.I(a,b),"")};_.M=function(a,b,c){return _.Lc(a,b,c==null?c:_.Sa(c))};_.N=function(a,b,c){return _.Lc(a,b,c==null?c:_.Ua(c))};_.O=function(a,b,c){return _.Lc(a,b,_.Va(c))};_.P=function(a,b,c){return _.Lc(a,b,c==null?c:_.Ta(c))};var Bb,Ab;_.Q=class{constructor(a,b,c){this.ha=_.ub(a,b,c)}toJSON(){return Cb(this)}Aa(a){try{return Ab=!0,a&&(Bb=a===kb||a!==jb&&a!==ob&&a!==rb?kb:a),JSON.stringify(Cb(this),$a)}finally{a&&(Bb=void 0),Ab=!1}}oc(){return _.Aa(this.ha)}};_.Q.prototype.Fd=_.Xa;_.Q.prototype.toString=function(){try{return Ab=!0,Cb(this).toString()}finally{Ab=!1}};_.Mc=_.Db();_.Nc=_.Db();_.Oc=_.Db();var Pc=class extends _.Q{constructor(a){super(a)}};_.Qc=class extends _.Q{constructor(a){super(a)}D(a){return _.N(this,3,a)}};var Rc=class extends _.Q{constructor(a){super(a)}Ic(a){return _.O(this,24,a)}};_.Sc=class extends _.Q{constructor(a){super(a)}};_.R=function(){this.qa=this.qa;this.Y=this.Y};_.R.prototype.qa=!1;_.R.prototype.isDisposed=function(){return this.qa};_.R.prototype.dispose=function(){this.qa||(this.qa=!0,this.O())};_.R.prototype[Symbol.dispose]=function(){this.dispose()};_.R.prototype.O=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Tc=class extends _.R{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}tb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].tb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Vc=class extends _.R{constructor(){var a=_.Uc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Wc=class extends _.Q{constructor(a){super(a)}};var Xc=class extends _.Q{constructor(a){super(a)}};var $c;_.Yc=function(a,b,c=98,d=new _.Qc){if(a.i){const e=new Pc;_.O(e,1,b.message);_.O(e,2,b.stack);_.N(e,3,b.lineNumber);_.P(e,5,1);_.F(d,40,e);a.i.log(c,d)}};$c=class{constructor(){var a=Zc;this.i=null;_.J(a,4,!0)}log(a,b,c=new _.Qc){_.Yc(this,a,98,c)}};var ad,bd;ad=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.gc(c,b,a)}catch(d){console.error(d)}}}};_.cd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new bd(a,b,c));ad(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.i=a;ad(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.j=a;ad(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
bd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.dd=a=>{var b="lc";if(a.lc&&a.hasOwnProperty(b))return a.lc;b=new a;return a.lc=b};_.ed=class{constructor(){this.v=new _.cd;this.i=new _.cd;this.D=new _.cd;this.B=new _.cd;this.C=new _.cd;this.A=new _.cd;this.o=new _.cd;this.j=new _.cd;this.F=new _.cd}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.dd(_.ed)}};var id;_.gd=function(){return _.E(_.fd,Rc,1)};_.hd=function(){return _.E(_.fd,_.Sc,5)};id=class extends _.Q{constructor(a){super(a)}};var jd;window.gbar_&&window.gbar_.CONFIG?jd=window.gbar_.CONFIG[0]||{}:jd=[];_.fd=new id(jd);var Zc=_.E(_.fd,Xc,3)||new Xc;_.gd()||new Rc;_.Uc=new $c;_.B("gbar_._DumpException",function(a){_.Uc?_.Uc.log(a):console.error(a)});_.kd=new Vc;var md;_.nd=function(a,b){var c=_.ld.i();if(a in c.i){if(c.i[a]!=b)throw new md;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Fb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.ld=class{constructor(){this.i={};this.j={}}static i(){return _.dd(_.ld)}};_.pd=class extends _.aa{constructor(){super()}};md=class extends _.pd{};_.B("gbar.A",_.cd);_.cd.prototype.aa=_.cd.prototype.then;_.B("gbar.B",_.ed);_.ed.prototype.ba=_.ed.prototype.M;_.ed.prototype.bb=_.ed.prototype.N;_.ed.prototype.bd=_.ed.prototype.qa;_.ed.prototype.bf=_.ed.prototype.Y;_.ed.prototype.bg=_.ed.prototype.L;_.ed.prototype.bh=_.ed.prototype.K;_.ed.prototype.bj=_.ed.prototype.J;_.ed.prototype.bk=_.ed.prototype.G;_.B("gbar.a",_.ed.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var qd=new Tc;_.nd("api",qd);
var rd=_.hd()||new _.Sc,sd=window,td=_.y(_.I(rd,8));sd.__PVT=td;_.nd("eq",_.kd);
}catch(e){_._DumpException(e)}
try{
_.ud=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var vd=class extends _.Q{constructor(a){super(a)}};var wd=class extends _.R{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.G(a,12)!=null&&(d.dpo=_.w(_.J(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.K(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.K(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.B("gapi.load",(0,_.z)(this.o,this));return this}};var xd=_.E(_.fd,_.Wc,14);if(xd){var yd=_.E(_.fd,_.ud,9)||new _.ud,zd=new vd,Ad=new wd;Ad.init(xd,yd,zd);_.nd("gs",Ad)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_sreeharshithavakkantham246@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./day3_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250106-060111_RC00_712437385'; var colabScsVersion = '931cdbea569e1f62eac28d8dbbd18e65'; var hl = 'en-GB'; var colabExperiments = JSON.parse('\x7b\x22add_prompt_cell\x22: false, \x22ai_banner\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22auto_open_chat_on_empty_notebook\x22: false, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_markdown_toolbar_tooltips\x22: true, \x22cell_output_actions_tooltip\x22: true, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_toolbar_tooltips\x22: true, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_announcements\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22gemini_rebrand\x22: true, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_duplicate_code\x22: true, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: false, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22interactive_sheet_next_steps\x22: true, \x22internal_chat\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22last_saved_indicator_refresh\x22: false, \x22latest_notebook_context_for_converse\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22minimizable_comments\x22: true, \x22ml_enabled\x22: true, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22move_converse_notebook_context_to_facts\x22: true, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: false, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prereq_cells_next_steps\x22: true, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22remove_ai_generate_fencing\x22: false, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: false, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: false, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.25\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_max_poll_count\x22: 45, \x22task_service_poll_interval_ms\x22: 2000, \x22task_service_wait_before_polling_ms\x22: 5000, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: true, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: false, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22want_completions_ai_consent_campaign\x22: false, \x22workstations\x22: false, \x22ids\x22: \x5b20730230, 20730357, 20730182, 20730252, 20730186, 20730315, 20730345, 20730351, 20730330, 20730265, 20730177, 20730150, 20730318, 20730297, 20730324, 20730262\x5d, \x22flag_ids\x22: \x7b\x22add_prompt_cell\x22: 45644995, \x22ai_banner\x22: 45670540, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22allowed_public_url_domains\x22: 45425558, \x22auto_open_chat_on_empty_notebook\x22: 45669599, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_markdown_toolbar_tooltips\x22: 45654223, \x22cell_output_actions_tooltip\x22: 45650940, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_toolbar_tooltips\x22: 45649981, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_announcements\x22: 45651325, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22gemini_rebrand\x22: 45631310, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_duplicate_code\x22: 45646291, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22interactive_sheet_next_steps\x22: 45634324, \x22internal_chat\x22: 45622872, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22last_saved_indicator_refresh\x22: 45672240, \x22latest_notebook_context_for_converse\x22: 45668776, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22minimizable_comments\x22: 45661083, \x22ml_enabled\x22: 45425493, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22move_converse_notebook_context_to_facts\x22: 45666389, \x22mpp_orc_temperature_override\x22: 45649914, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prereq_cells_next_steps\x22: 45640400, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'sreeharshithavakkantham246@gmail.com'; var colabRenderDataToken = 'AFWLbD0uugP35md2AQ5l3FQK-EsCYdpaEMicce3didXZOl-ht51D_6e1PSagsDOleffxby57_CgyceN1CJPWsKgAFIx1UAPjmrIz-4y4'; var colabConfig = '\x5b\x5b\x22sreeharshithavakkantham246@gmail.com\x22,\x5b1,\x22AHXL0D2MlU\/UeNubdUgYHm6KVWEZhGWTyw9b9vrOEihSBtF\/azz4diHREmYsIGnW3eB+eofbxOA4c7Hg8FPE2ow3NWUoEepI3tYrQwqA8mw8LE2rzW38KOeVz7Amd8MiDjgDpTL0eD7X6aH\/89OsouZJN\/w9gXbnNNTsO8yC+s1zA9SCpYOx5ayRn6y+BZRGEuif5k7dW\/r25O435z5hrm8IV7nWhV\/rjK6OvDOYcpGcBma4kCoMqroKX3bvVHeA\/Z\/YN6H+9RUf+21v5oP9MExDnc8IagCuVw2ih24\/XpYE0\/k6XgsPZms4ajvgKovJx2i5jkFRQbmcmbMe+aKD+lpigah\/mNxupwcwtL98GlrvnXzkEekSa7XcaJrZczrSrSGtB3I6iRjmAmRO79VM6DJ2VqL6NR9uEbxVEZPTKyhuA29n3qycngF7Lr7ndmTNC15epw7eW5BBeonScQkwKs2GvnNWdpU7AxRngZSYjMWJ2puNiL\/9bMZgtVO+JeIqmyJTPWfvMYdWZW2OGJZyCEYJPKDVFJgvX5fNfH4P6aATah33RUPkNuKZ4gXQywfnI7T0GS6U4or0F8u+hjYxfSIpjCOwYKhTPUH8VFJn8CvGwXu\/Qo2C\/sLq+RHkBVyA7OKlnt70czPF2\/r0FXfDekKG6A3wkiI0QsfckUxD1rQcPlQ8TlARs5uMPYuHSoB801s9bE10QwfnB6xcVp\/C4WMngDGglngYursdRotN8QSIThIrx21kQ6beHN2Sbey2JSqQ4ahEAMrxSe8AdYjV+FFnPYOsZV0uQdEUPjqzXmw+LUB6k8bokeKxlK3H7KAH7NJ5cCpiL+h+gv+80QIXJmxEGgo+eXZE9\/5jPeo3XYAORphw2b2GrAqXdsZNTY5qu5E7TKOI3C0RJPUNqye49d+3NQhMnDuKMshJpD+uKHik27lTJC80OM6kTMgnT3lzehpV7YeM14Z86dMteH+GdkuX0ie4ijF6YS6V2+cYS8k9gTIHF6lpY9+dgZgIOxtajf5tvwjReOgQIyhRjAW59CYDlhx5bIHN8rT107HCpJEWuIwhRmvvZbYt0NsYv\/RVT7e\/xOZI4g07bh4t7N9UTdpZLhILg8\/\/VCDLYN8sUM4wxca9ytWMvmxVOpTbMc1IKDh74AGOO\/VvtGHzd2BhY6sW51xbSLsfl5lmjLMRHsDmxnKBZX2mIElR54Gz5B9RhuIlWnERyF8RKQ8lZpKMlKubeeYMR4CYC4RN4UeUWhwYTrRf7gFnCkPv8DRecrziakLmEbyVO11kJsipvc16STX3IKlT9DwNXH9ys2AckUZDIGjjmjHcHafu7C30A4r9dYPPlo7bZHWBdeKROTk1O0VrZuA8ta05DG\/OAoiaoNGKKSZII4X5qFhPoql\/bbKZil8kPBD\/cXzZOPvuBD1xpMTQtN0dhMOB7KciWT26UMI7mAWf8TgQQZD42k8WjRNV67gl7L2fH+3+kNW4vwd+IHo3BA43YyIZW45sCx3KC0uG0mMNJTWNmqroK8mHb4g7hsK22VcbpNEwEVfWf5+wAipXcDsPahGK1xrBXKWsVJ92WMf1m3+HCEgkj3L\/XuKPwMS0oPAlft4d1gI2zF75zCzzxGtXKEvNFsxdkKvmXJZKffrnOhwV8F4KJQ7GHBb85tpxZkXGyv9AtW\/LqPCodscFTtB6j8+FHwzGPbFG3gNud04VcZN3ZU3y3RwaMR3\/0QuO83b5sjGpfaop42hgem6w\/4QU9bNprbnaNMPFsWvtNannPD0zmXGzKDgSk8OdqCENHqGAD1CRA9RBhd4qIQMbED5\/QTvTY7Ys8jvZDYoMM3+cdEYolLkA+9cSth3jHxjv4MN\/PQ\/F3gu173GnKuFxKjeckvc\/cxynwWtMz2epwPa+JzDl75s\x3d\x22,\x22AJ9oCCxS0ZQffMIoVAdV6JT26o3JAUoi9RQXOsais5\/3YrEb8O\/sO7WxwUevdc5kx14qLhM62\/Nis+z8KQXeiINZvgFo5R3hVg2dCf705BvuYAg3Ou4xSaUj7lM8DkOlCy6of8pF\/A6U\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22\x5d,\x5b1,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/931cdbea569e1f62eac28d8dbbd18e65/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./day3_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./day3_files/rs=AA2YrTvH0Rknr6hXqx-tgqAUuIv05wLZhQ" nonce=""></script><link type="text/css" href="./day3_files/rs=AA2YrTvDtorsWuiBHYzP5-lS7pwgoAa95g" rel="stylesheet"><style type="text/css"><br>* {<br>  -webkit-user-select: text !important;<br>  -moz-user-select: text !important;<br>  -ms-user-select: text !important;<br>   user-select: text !important;<br>}<br></style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./day3_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./day3_files/editor.main.css"><script async="async" type="text/javascript" src="./day3_files/editor.main.nls.js.download"></script><script src="./day3_files/api.js.download" nonce=""></script><script src="./day3_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-insertedLineBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #6aa94f; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #f28b82; }
.mtk11 { color: #d7ba7d; }
.mtk12 { color: #dcdcdc; }
.mtk13 { color: #808080; }
.mtk14 { color: #4ec9b0; }
.mtk15 { color: #dcdcaa; }
.mtk16 { color: #f44747; }
.mtk17 { color: #82c6ff; }
.mtk18 { color: #c586c0; }
.mtk19 { color: #a79873; }
.mtk20 { color: #dd6a6f; }
.mtk21 { color: #5bb498; }
.mtk22 { color: #909090; }
.mtk23 { color: #778899; }
.mtk24 { color: #ff00ff; }
.mtk25 { color: #b46695; }
.mtk26 { color: #ff0000; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #3dc9b0; }
.mtk29 { color: #74b0df; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" data-new-gr-c-s-check-loaded="14.1215.0" data-gr-ext-installed="" data-new-gr-c-s-loaded="14.1215.0" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./day3_files/gapi_loader.js.download" nonce=""></script><script src="./day3_files/socketio_binary.js.download" nonce=""></script><script src="./day3_files/analytics_binary.js.download" nonce=""></script><script src="./day3_files/MathJax.js.download" nonce=""></script><script src="./day3_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./day3_files/external_binary_l10n__en_gb.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$342480955$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$342480955$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$342480955$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$342480955$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Loading…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_R" ng-non-bindable=""><div class="gb_Ac"><div>Google Account</div><div class="gb_g">Sree harshitha Vakkantham</div><div>sreeharshithavakkantham246@gmail.com</div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Fd;Fd=class extends _.pd{};_.Gd=function(a,b){if(b in a.i)return a.i[b];throw new Fd;};_.Hd=function(a){return _.Gd(_.ld.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Kd;_.Id=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Kd=function(a){return new _.Jd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Ld=globalThis.trustedTypes;_.Md=class{constructor(a){this.i=a}toString(){return this.i}};_.Nd=new _.Md("about:invalid#zClosurez");_.Jd=class{constructor(a){this.nh=a}};_.Od=[Kd("data"),Kd("http"),Kd("https"),Kd("mailto"),Kd("ftp"),new _.Jd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Pd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Qd=new _.Pd(_.Ld?_.Ld.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Ud,he,Td,Vd,$d;_.Rd=function(a){return a==null?a:Number.isFinite(a)?a|0:void 0};_.Sd=function(a){if(a==null)return a;if(typeof a==="string"){if(!a)return;a=+a}if(typeof a==="number")return Number.isFinite(a)?a|0:void 0};Ud=function(){let a=null;if(!Td)return a;try{const b=c=>c;a=Td.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Wd=function(){Vd===void 0&&(Vd=Ud());return Vd};
_.Yd=function(a){const b=_.Wd();return new _.Xd(b?b.createScriptURL(a):a)};_.Zd=function(a){if(a instanceof _.Xd)return a.i;throw Error("F");};_.ae=function(a){if($d.test(a))return a};_.be=function(a){if(a instanceof _.Md)if(a instanceof _.Md)a=a.i;else throw Error("F");else a=_.ae(a);return a};_.ce=function(a,b=document){let c,d;b=(d=(c="document"in b?b.document:b).querySelector)==null?void 0:d.call(c,`${a}[nonce]`);return b==null?"":b.nonce||b.getAttribute("nonce")||""};
_.de=function(a){var b=_.Ra(a);return b=="array"||b=="object"&&typeof a.length=="number"};_.ee=function(a,b,c){return _.yb(a,b,c,!1)!==void 0};_.fe=function(a,b){return _.Sd(_.Kc(a,b))};_.S=function(a,b){return _.Rd(_.Kc(a,b))};_.T=function(a,b,c=0){return _.zb(_.fe(a,b),c)};_.ge=function(a,b,c=0){return _.zb(_.S(a,b),c)};_.ie=function(a,b){return a.lastIndexOf(b,0)==0};Td=_.Ld;_.Xd=class{constructor(a){this.i=a}toString(){return this.i+""}};$d=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var ne,re,je;_.le=function(a){return a?new je(_.ke(a)):he||(he=new je)};_.me=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.U=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.oe=function(a,b){_.Eb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:ne.hasOwnProperty(d)?a.setAttribute(ne[d],c):_.ie(d,"aria-")||_.ie(d,"data-")?a.setAttribute(d,c):a[d]=c})};ne={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.pe=function(a){return a?a.defaultView:window};_.se=function(a,b){const c=b[1],d=_.qe(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.oe(d,c));b.length>2&&re(a,d,b);return d};re=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.de(f)||_.Nb(f)&&f.nodeType>0?d(f):_.gc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Id(f):f,d)}};
_.te=function(a){return _.qe(document,a)};_.qe=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ue=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.ve=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.we=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ke=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};je=function(a){this.i=a||_.t.document||document};_.m=je.prototype;
_.m.H=function(a){return _.me(this.i,a)};_.m.Wa=function(a,b,c){return _.se(this.i,arguments)};_.m.appendChild=function(a,b){a.appendChild(b)};_.m.xe=_.ue;_.m.Sf=_.ve;_.m.Rf=_.we;
}catch(e){_._DumpException(e)}
try{
_.Gi=function(a){const b=_.ce("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Hi=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.Yd(a);return b};_.Ii=class extends _.Q{constructor(a){super(a)}};_.Ji=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Li=function(a,b,c){a<b?Ki(a+1,b):_.Uc.log(Error("da`"+a+"`"+b),{url:c})},Ki=function(a,b){if(Mi){const c=_.te("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Zd(Mi);_.Gi(c);c.onerror=_.Qb(Li,a,b,c.src);_.Ji("HEAD")[0].appendChild(c)}},Ni=class extends _.Q{constructor(a){super(a)}};var Oi=_.E(_.fd,Ni,17)||new Ni,Pi,Mi=(Pi=_.E(Oi,_.Ii,1))?_.Hi(Pi):null,Qi,Ri=(Qi=_.E(Oi,_.Ii,2))?_.Hi(Qi):null,Si=function(){Ki(1,2);if(Ri){const a=_.te("LINK");a.setAttribute("type","text/css");a.href=_.Zd(Ri).toString();a.rel="stylesheet";let b=_.ce("style",window);b&&a.setAttribute("nonce",b);_.Ji("HEAD")[0].appendChild(a)}};(function(){const a=_.gd();if(_.G(a,18))Si();else{const b=_.fe(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Si,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script type="text/javascript" src="chrome-extension://fpjppnhnpnknbenelmbnidjbolhandnf/content_script_web_accessible/ecp_regular.js"></script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./day3_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/drive/1UdRycuunGeBiQZGSa7vClz3GrLgZCkRn#top-toolbar"><!--?lit$342480955$-->Skip to main content</a></template></colab-header-skip-button>
    <!--?lit$342480955$-->
    <!--?lit$342480955$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$342480955$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1UdRycuunGeBiQZGSa7vClz3GrLgZCkRn#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close"><!--?lit$342480955$-->
    <!--?lit$342480955$--><i class="material-icons"><!--?lit$342480955$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        
    <!--?lit$342480955$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><div id="header-logo">
              <!--?lit$342480955$--> <!--?lit$342480955$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$342480955$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$342480955$--> <!--?lit$342480955$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" fdprocessedid="dwfpj9" style="width: 127.7px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Untitled1.ipynb_</colab-input-sizer>
            <!--?lit$342480955$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$342480955$-->
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$342480955$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$342480955$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$342480955$-->All changes saved</button></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$342480955$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$342480955$-->
      <!--?lit$342480955$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$342480955$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$342480955$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$342480955$--> <md-text-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->people</md-icon>
                <!--?lit$342480955$-->Share
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ea gb_Id gb_2d gb_Vc" id="gb"><div class="gb_Bd gb_Zd gb_wd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Re" style="display:block"><div class="gb_2c"></div><div class="gb_y gb_bd gb_Nf gb_Z"><div class="gb_C gb_ib gb_Nf gb_Z"><a class="gb_A gb_Xa gb_Z" aria-expanded="false" aria-label="Google Account: Sree harshitha Vakkantham  
(sreeharshithavakkantham246@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en-GB&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_O gbii" src="./day3_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyhTWTBQFsP9Y0q_Km_m4Innu1LHgsmm7GKymy_3HCp4GTtE=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyhTWTBQFsP9Y0q_Km_m4Innu1LHgsmm7GKymy_3HCp4GTtE=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""><div class="gb_P gb_Q" aria-hidden="true"><svg class="gb_Ja" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Ka" cx="7" cy="7" r="7"></circle><path class="gb_Ma" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Bd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Bd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("B`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Cd=document.querySelector(".gb_I .gb_A"),Dd=document.querySelector("#gb.gb_Rc");Cd&&!Dd&&_.Bd(_.kd,Cd,"click");
}catch(e){_._DumpException(e)}
try{
_.gh=function(a){const b=[];let c=0;for(const d in a)b[c++]=a[d];return b};_.hh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ma()&&a.i[b].B())return a.i[b];return null};_.ih=function(a,b){a.i[b.K()]=b};var jh=new class extends _.R{constructor(){var a=_.Uc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.hh(this)&&_.hh(this).K()==a||this.i[a].R(!0))}Qa(a){this.j=a;for(const b in this.i)this.i[b].ma()&&this.i[b].Qa(a)}hc(a){return a in this.i?this.i[a]:null}};_.nd("dd",jh);
}catch(e){_._DumpException(e)}
try{
_.Ai=function(a,b){return _.M(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Bi=document.querySelector(".gb_y .gb_A"),Ci=document.querySelector("#gb.gb_Rc");Bi&&!Ci&&_.Bd(_.kd,Bi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$342480955$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->search</md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variables" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->folder</md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button command="snippets" data-aria-label="Code snippets" title="Code snippets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->code</md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button command="show-command-palette" data-aria-label="Command palette" title="Command palette" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Command palette">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$342480955$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->terminal</md-icon>
    </md-icon-button> <!--?lit$342480955$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$342480955$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
        <!--?lit$342480955$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$342480955$--><span class="screenreader-only"><!--?lit$342480955$-->Insert code cell below <!--?lit$342480955$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$342480955$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$342480955$-->Code
          </colab-toolbar-button>
          <!--?lit$342480955$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
        <!--?lit$342480955$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$342480955$--><span class="screenreader-only"><!--?lit$342480955$-->Add text cell <!--?lit$342480955$--></span>
      </md-text-button>
      <!--?lit$342480955$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$342480955$-->Text
          </colab-toolbar-button>
        
    <!--?lit$342480955$-->
    <!--?lit$342480955$-->
    <!--?lit$342480955$-->
    <!--?lit$342480955$-->
    <!--?lit$342480955$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$342480955$-->All changes saved</button></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$342480955$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$342480955$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$342480955$--><!--?lit$342480955$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$342480955$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connected to
Python 3 Google Compute Engine backend
RAM: 1.01 GB/12.67 GB
Disk: 32.66 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
        <!--?lit$342480955$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$342480955$--><span class="screenreader-only"><!--?lit$342480955$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.01 GB/12.67 GB
Disk: 32.66 GB/107.72 GB <!--?lit$342480955$--></span>
      </md-text-button>
      <!--?lit$342480955$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to
Python 3 Google Compute Engine backend
RAM: 1.01 GB/12.67 GB
Disk: 32.66 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Connected to</div><!----><!----><div><!--?lit$342480955$-->Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$342480955$-->RAM: 1.01 GB/12.67 GB</div><!----><!----><div><!--?lit$342480955$-->Disk: 32.66 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$342480955$--> <div id="connect-button-resource-display">
        <!--?lit$342480955$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$342480955$-->RAM</div>
      <!--?lit$342480955$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$342480955$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$342480955$-->Disk</div>
      <!--?lit$342480955$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$342480955$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$342480955$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$342480955$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="spark"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
        <!--?lit$342480955$-->
    <svg slot="icon" viewBox="0 -960 960 960" width="24" height="24">
      <defs>
        <lineargradient id="sparkGradient" x1="0" y1="1" x2="1" y2="0">
          <stop offset="33.06%" stop-color="#217BFE"></stop>
          <stop offset="44.4%" stop-color="#078EFB"></stop>
          <stop offset="65.69%" stop-color="#A190FF"></stop>
          <stop offset="75.05%" stop-color="#BD99FE"></stop>
        </lineargradient>
      </defs>
      <path fill="url(#sparkGradient)" d="M480-80q2 0 2-2 0-82 31-154t85-126q54-54 126-85t154-31q2 0 2-2t-2-2q-82 0-154-31t-126-85q-54-54-85-126t-31-154q0-2-2-2t-2 2q0 82-31 154t-85 126q-54 54-126 85T82-482q-2 0-2 2t2 2q82 0 154 31t126 85q54 54 85 126t31 154q0 2 2 2Z"></path>
    </svg>
        <span class="button-content"><slot></slot></span>
        <!--?lit$342480955$--><span class="screenreader-only"><!--?lit$342480955$--> <!--?lit$342480955$--></span>
      </md-text-button>
      <!--?lit$342480955$--><!--?--></template>
            <!--?lit$342480955$-->Gemini
          </colab-toolbar-button>
    <!--?lit$342480955$-->
    <span class="collapsed-options">
      <!--?lit$342480955$--><span class="colab-separator"></span>
      <!--?lit$342480955$--> <md-icon-button command="share" title="Share notebook" data-aria-label="Share notebook" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->people</md-icon>
          </md-icon-button><md-icon-button command="preferences" data-aria-label="Open settings" title="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$342480955$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$342480955$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$342480955$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-g6Oja1_duWcb" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$342480955$--><div class="indicator"></div>
      </div>
      <!--?lit$342480955$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-g6Oja1_duWcb"><!--?lit$342480955$--><!--?lit$342480955$-->Notebook<!--?--></span>
            <!--?lit$342480955$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$342480955$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$342480955$-->
              <div class="notebook-content ">
                <!--?lit$342480955$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$342480955$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$342480955$-->Text
        </md-outlined-button>
        <!--?lit$342480955$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code icon-scrolling focused code-has-output" id="cell-QWEJysFJvmcq" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----> <md-icon-button class="colab-icon" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->arrow_upward</md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Move cell up</div><!----><!----><div><!--?lit$342480955$-->Ctrl+M K</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" aria-disabled="true">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->arrow_downward</md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Move cell down</div><!----><!----><div><!--?lit$342480955$-->Ctrl+M J</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----><!--?lit$342480955$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-QWEJysFJvmcq" anchor="ai-menu-anchor-QWEJysFJvmcq" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$342480955$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$342480955$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$342480955$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$342480955$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$342480955$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$342480955$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$342480955$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$342480955$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$342480955$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$342480955$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$342480955$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$342480955$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$342480955$-->Explain code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button class="colab-icon" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-QWEJysFJvmcq-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-QWEJysFJvmcq" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-QWEJysFJvmcq" id="ai-menu-anchor-QWEJysFJvmcq-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Available AI features</div><!----><!--?--></template>
              </colab-tooltip-trigger> <!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->link</md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Copy link to cell</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->comment</md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Add a comment</div><!----><!----><div><!--?lit$342480955$-->Ctrl+Alt+M</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->settings</md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Open editor settings</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->edit</md-icon>
            <!--?lit$342480955$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->edit_off</md-icon>
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Edit</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Mirror cell in tab</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->delete</md-icon>
            <!--?lit$342480955$-->
          </md-icon-button>
          <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Delete cell</div><!----><!----><div><!--?lit$342480955$-->Ctrl+M D</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!--?lit$342480955$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="colab-icon cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->More cell actions</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell">
        <span class="execution-count"><!--?lit$342480955$-->[7]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$342480955$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$342480955$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$342480955$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by Sree harshitha Vakkantham
12:40 (0 minutes ago)
executed in 0.323 s"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$342480955$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$342480955$-->executed by Sree harshitha Vakkantham</div><!----><!----><div><!--?lit$342480955$-->12:40 (0 minutes ago)</div><!----><!----><div><!--?lit$342480955$-->executed in 0.323 s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$342480955$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$342480955$-->0s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="9" data-mode-id="notebook-python" style="height: 409px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/7" style="width: 1398px; height: 409px;"><div data-mprt="3" class="overflow-guard" style="width: 1398px; height: 409px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 409px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 409px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 409px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1392px; height: 409px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 409px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1392px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="current-line" style="width:1392px; height:19px;"></div></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1392px; height: 409px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1">a1&nbsp;=&nbsp;</span><span class="mtk6">85</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">b1&nbsp;=&nbsp;</span><span class="mtk6">92</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">c1&nbsp;=&nbsp;</span><span class="mtk6">88</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Calculate&nbsp;average&nbsp;marks</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1">d1&nbsp;=&nbsp;</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">a1&nbsp;+&nbsp;b1&nbsp;+&nbsp;c1</span><span class="mtk12 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;/&nbsp;</span><span class="mtk6">3</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Determine&nbsp;grade</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk18">if</span><span class="mtk1">&nbsp;d1&nbsp;&gt;=&nbsp;</span><span class="mtk6">90</span><span class="mtk12">:</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=&nbsp;</span><span class="mtk5">"Grade:&nbsp;A"</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk18">elif</span><span class="mtk1">&nbsp;</span><span class="mtk6">80</span><span class="mtk1">&nbsp;&lt;=&nbsp;d1&nbsp;&lt;&nbsp;</span><span class="mtk6">90</span><span class="mtk12">:</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=&nbsp;</span><span class="mtk5">"Grade:&nbsp;B"</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk18">elif</span><span class="mtk1">&nbsp;</span><span class="mtk6">70</span><span class="mtk1">&nbsp;&lt;=&nbsp;d1&nbsp;&lt;&nbsp;</span><span class="mtk6">80</span><span class="mtk12">:</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=&nbsp;</span><span class="mtk5">"Grade:&nbsp;C"</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk18">else</span><span class="mtk12">:</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=&nbsp;</span><span class="mtk5">"Grade:&nbsp;Fail"</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span><span class="mtk8">#&nbsp;Print&nbsp;results</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk9">f</span><span class="mtk5">"Average&nbsp;Marks:&nbsp;</span><span class="mtk12 bracket-highlighting-1">{</span><span class="mtk1">d1</span><span class="mtk6">:.2f</span><span class="mtk12 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">grade</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1392px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 361px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1378px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1378px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="511" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 409px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 409px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 409px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1398px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 361px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1398px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 409px;"><div class="minimap-shadow-hidden" style="height: 409px;"></div><canvas width="0" height="511" style="position: absolute; left: 0px; width: 0px; height: 409px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="511" style="position: absolute; left: 0px; width: 0px; height: 409px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 51px; width: 276px; z-index: 50; display: none; visibility: hidden; max-width: 1523px; top: 444.6px; left: 230.4px;"><div class="monaco-sash vertical" style="left: 274px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal disabled" style="top: 49px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 276px; height: 51px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 922.68px; max-height: 250px; width: 276px; height: 51px;"><div class="hover-row"><div class="marker hover-contents" style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><span style="white-space: pre-wrap;">Unexpected indentation</span></div></div><div class="hover-row status-bar"><div class="actions"><div class="action-container" tabindex="0"><a class="action" role="button"><span>View Problem (Alt+F8)</span></a></div><div>No quick fixes available</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 266px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 266px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 51px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 51px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$342480955$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$342480955$--><!----><div><!--?lit$342480955$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Average Marks: 88.33
Grade: B
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$342480955$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$342480955$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$342480955$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style=""></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$342480955$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$342480955$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$342480955$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$342480955$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$342480955$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$342480955$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$342480955$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./day3_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./day3_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$342480955$--> <div class="connect-status">
        <md-icon status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$--><svg viewBox="0 0 24 24"><!--?lit$342480955$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
        <div aria-atomic="true" aria-live="polite"><!--?lit$342480955$-->Connected to Python 3 Google Compute Engine backend</div>
      </div>
      <md-icon-button class="visible-on-closed" title="Connected" disabled="" value="" data-aria-label="Connected"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Connected" disabled="">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$342480955$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$342480955$-->
      <md-icon-button title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$342480955$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$342480955$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$342480955$--><span class="icon"><slot></slot></span>
        <!--?lit$342480955$-->
        <!--?lit$342480955$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Locate in Drive<!--?lit$342480955$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Open in playground mode<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->New notebook in Drive<!--?lit$342480955$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Open notebook<!--?lit$342480955$--></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Upload notebook<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Rename<!--?lit$342480955$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Move<!--?lit$342480955$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Move to the bin<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Save a copy in Drive<!--?lit$342480955$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Save a copy as a GitHub Gist<!--?lit$342480955$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Save a copy in GitHub<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Save<!--?lit$342480955$--></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Save and pin revision<!--?lit$342480955$--></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Revision history<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$342480955$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Print<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Download .ipynb<!--?lit$342480955$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Download .py<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Undo<!--?lit$342480955$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Redo<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Select all cells<!--?lit$342480955$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Cut cell or selection<!--?lit$342480955$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Copy cell or selection<!--?lit$342480955$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Paste<!--?lit$342480955$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Delete selected cells<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Find and replace<!--?lit$342480955$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Find next<!--?lit$342480955$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Find previous<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Notebook settings<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Clear all outputs<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$342480955$-->Table of contents<!--?lit$342480955$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Notebook info<!--?lit$342480955$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Executed code history<!--?lit$342480955$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$342480955$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1e" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Collapse sections<!--?lit$342480955$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Expand sections<!--?lit$342480955$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Save collapsed section layout<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Show/hide code<!--?lit$342480955$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Show/hide output<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1l" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Focus next tab<!--?lit$342480955$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Focus previous tab<!--?lit$342480955$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Move tab to next pane<!--?lit$342480955$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Move tab to previous pane<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Hide comments<!--?lit$342480955$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Minimise comments<!--?lit$342480955$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Expand comments<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Code cell<!--?lit$342480955$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Text cell<!--?lit$342480955$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Section header cell<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Scratch code cell<!--?lit$342480955$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Code snippets<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1x" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Add a form field<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Run all<!--?lit$342480955$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Run before<!--?lit$342480955$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Run the focused cell<!--?lit$342480955$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Run selection<!--?lit$342480955$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Run cell and below<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":25" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Interrupt execution<!--?lit$342480955$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":27" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Restart session<!--?lit$342480955$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Restart session and run all<!--?lit$342480955$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Disconnect and delete runtime<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2a" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Change runtime type<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Manage sessions<!--?lit$342480955$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->View resources<!--?lit$342480955$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->View runtime logs<!--?lit$342480955$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Command palette<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Settings<!--?lit$342480955$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Keyboard shortcuts<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2l" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Diff notebooks<!--?lit$342480955$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$342480955$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$342480955$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Frequently asked questions<!--?lit$342480955$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->View release notes<!--?lit$342480955$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Search code snippets<!--?lit$342480955$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2r" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Report a bug<!--?lit$342480955$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Report Drive abuse<!--?lit$342480955$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->Send feedback<!--?lit$342480955$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->View Terms of Service<!--?lit$342480955$--></div></div><div command="view-in-english" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$342480955$-->View in English<!--?lit$342480955$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$342480955$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$342480955$--><button id="button" class="button">
      <!--?lit$342480955$-->
      <span class="touch"></span>
      <!--?lit$342480955$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$342480955$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$342480955$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy21b0ae53f9be04f3c9c656297abd40a54eaf02700.486242685" name="apiproxy21b0ae53f9be04f3c9c656297abd40a54eaf02700.486242685" src="./day3_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-5kvdtnoj25xo" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./day3_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./day3_files/saved_resource.html"></iframe></div><span id="PING_IFRAME_FORM_DETECTION" style="display: none;"></span><iframe src="./day3_files/bscframe.html" style="display: none;"></iframe></body><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;limited&quot;,&quot;isActive&quot;:false,&quot;isUserDisabled&quot;:false}"></div></template></grammarly-desktop-integration></html>