def convert_df(input_df):
    df_html = input_df.to_html(index=False, escape=False, formatters=dict(MODAL_IMG=image_formatter, CANAL=image_formatter))
    
    html_with_container = f'''
        <html>
        <head>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
            <style>
                .table-container {{
                    height: 400px;
                    width: 100%;
                    overflow-y: auto;
                    border: 2px solid #444;
                }}
                .table-container:hover {{ border-color: red; }}
                table {{ width: 100%; }}
                td {{ padding: 24px; background: #eee; }}
            </style>
        </head>
        <body>
            <div class="table-container" id="table-container">
                {df_html}
            </div>
            <script>
                var $container = $("#table-container");
                function anim() {{
                    var st = $container.scrollTop();
                    var sb = $container.prop("scrollHeight") - $container.innerHeight();
                    $container.animate({{scrollTop: st < sb / 2 ? sb : 0}}, 4000, anim);
                }}
                function stop() {{
                    $container.stop();
                }}
                anim();
                $container.hover(stop, anim);
            </script>
        </body>
        </html>
        '''
    return html_with_container

html = convert_df(df)
st.markdown(html, unsafe_allow_html=True)