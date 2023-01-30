import stweet as st

def Bocchi_scrap():
    user_task = st.GetUsersTask(['BTR_anime'])
    output_json = st.JsonLineFileRawOutput('output_raw_user.jl')
    output_print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()
    
if __name__ == '__main__':
    Bocchi_scrap()