from socketserver import ForkingTCPServer
from turtle import title
import dash
from dash import Dash, dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class dashboard(object):
    def __init__(self):
        self.night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)',
                             'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
        self.sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                                  'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
        self.irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                              'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
        self.cafe_colors = ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                            'rgb(175, 51, 21)', 'rgb(35, 36, 21)']
        self.col0 = ['cluster0']*2+['cluster1']*2+['cluster2']*2+['cluster3']*2

    # ======================== Plotly Graphs
    # ================================================= NAV>500 ============================================

    def segmentation1(self):
        col0 = ['cluster0', 'cluster1', 'cluster2', 'cluster3']
        col1 = [8296, 6888, 10090, 7278]
        fig = go.Figure(
            data=[go.Pie(labels=col0, values=col1, pull=[0, 0, 0.2, 0], textfont_size=14)])
        return fig.update_layout(title='Clusters'), len(col0)

    def loan_value_average1(self):
        colx = 'cluster'
        coly = 'Loan value average (ty VND)'
        df0 = self.gen(0, 0, 0, 0, 0, 0, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 0.088, 0.016, 0.0506, 0.1114, 0.01, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 0.4, 0.2115, 0.35123, 0.555, 0.01, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(0, 0, 0, 0, 0, 0, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3).update_layout(
            title='Loan value average')

    def der_transaction_value_average1(self):

        col0 = ['cluster0']*2+['cluster1']*2+['cluster2']*2+['cluster3']*2
        col1 = ['zero', 'not zero']*4
        col2 = [95.7, 100-95.7, 90.5, 100-90.5, 87.8, 100-87.8, 100, 0]
        data = pd.DataFrame(
            {'cluster': col0, 'zero or not': col1, 'percent': col2})
        fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'domain'}, {
                            'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]])
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster0']['zero or not'], values=data[data['cluster'] == 'cluster0']['percent'], name="cluster0", marker_colors=self.night_colors),
                      1, 1)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster1']['zero or not'], values=data[data['cluster'] == 'cluster1']['percent'], name="cluster1", marker_colors=self.sunflowers_colors),
                      1, 2)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster2']['zero or not'], values=data[data['cluster'] == 'cluster2']['percent'], name="cluster2", marker_colors=self.irises_colors),
                      2, 1)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster3']['zero or not'], values=data[data['cluster'] == 'cluster3']['percent'], name="cluster3", marker_colors=self.cafe_colors),
                      2, 2)

        fig.update_traces(hole=.4, hoverinfo="label+percent+name")
        fig.update_layout(
            title_text="der transaction value average",
            annotations=[dict(text='cluster0', x=0.19, y=0.82, font_size=13, showarrow=False),
                         dict(text='cluster1', x=0.81, y=0.82,
                              font_size=13, showarrow=False),
                         dict(text='cluster2', x=0.19, y=0.19,
                              font_size=13, showarrow=False),
                         dict(text='cluster3', x=0.81, y=0.19, font_size=13, showarrow=False)])
        fig = go.Figure(fig)
        return fig.update_layout(
            title='Der transaction value average')

    def Stock_total_order_average1(self):
        colx = 'cluster'
        coly = 'Stock total order average'
        df0 = self.gen(5, 6.5, 2.67, 5.67, 9.5, 1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(5, 8.4, 4.5, 7.83, 11.83, 1, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(5, 9.5, 5.5, 9.33, 13.167, 1, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(5, 0.44, 0, 0, 0, 1, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def Stock_transaction_value_average1(self):
        colx = 'cluster'
        coly = 'Stock transaction value average (ty VND)'
        df0 = self.gen(2, 5.3, 1.4, 3.05, 6.28, 1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 9.98, 3, 6.1, 12, 1, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 16, 0.657, 12, 22.2, 1, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(2, 0, 0, 0, 0, 1, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def NAV1(self):
        colx = 'cluster'
        coly = 'NAV (ty VND)'
        df0 = self.gen(2, 1.3, 0.629, 0.874, 1.39, 1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 1.43, 0.659, 0.959, 1.58, 1, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 1.1, 0.6412, 0.8666, 1.29, 1, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(2, 2.2, 0.836, 1.4, 2.83, 1, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def time_open1(self):
        colx = 'cluster'
        coly = 'Time open (ty VND)'
        df0 = self.gen(2, 360, 167, 253, 416, 100, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 371, 184, 274, 441, 100, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 380, 204, 311, 461, 100, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(2, 606, 223, 463, 913, 100, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def city_of_star1(self):
        col1 = ['cluster0']*4+['cluster1']*4+['cluster2']*4+['cluster3']*2
        col2 = ['HN', 'HCM', 'Others', 'DSVN']*3+['HN', 'HCM']
        col3 = [51.4, 14.6, 6.2, 6.1, 48.4, 15.3,
                5.9, 6, 41.4, 17.3, 6, 6, 62.2, 9.2]
        col4 = [8296]*4+[6888]*4+[10090]*4+[7278]*2
        data = pd.DataFrame({'cluster': col1, 'city': col2,
                            'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="city", title="City of Star")
        return fig

    def business1(self):
        col1 = ['cluster0']*4+['cluster1']*4+['cluster2']*4+['cluster3']*4
        col2 = ['TVDT', 'DVKH', 'TVTC', 'DOI TAC']*4
        col3 = [86.5, 10.4, 1.7, 1.5, 93.2, 4, 1, 0.7,
                95.6, 3.2, 0.9, 0.3, 3, 1.6, 70.6, 24.7]
        col4 = [8296]*4+[6888]*4+[10090]*4+[7278]*4
        data = pd.DataFrame(
            {'cluster': col1, 'Business party': col2, 'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="Business party", title="Business")
        return fig

    def product1(self):

        col1 = ['cluster0']*2+['cluster1']*2+['cluster2']*2+['cluster3']*3
        col2 = ['1', '3']*3+['1', '2', '3']
        col3 = [94.2, 5.8, 89.6, 10.3, 96.9, 3.1, 89, 0.3, 10.8]
        col4 = [8296]*2+[6888]*2+[10090]*2+[7278]*3
        data = pd.DataFrame(
            {'cluster': col1, 'product status': col2, 'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="product status", title="product")
        return fig

    def age1(self):
        col1 = ['cluster0']*6+['cluster1']*6+['cluster2']*6+['cluster3']*6
        col2 = [1, 2, 3, 4, 5, 6]*4
        col3 = [1.1, 2.2, 11.9, 49.2, 24.2, 11.3, 1.2, 2, 12.2, 51.7, 22.7,
                10.3, 1.1, 2.3, 14, 53.9, 20.9, 7.6, 0.6, 0.8, 5.2, 22.4, 24.7, 46.3]
        col4 = [8296]*6+[6888]*6+[10090]*6+[7278]*6
        data = pd.DataFrame({'cluster': col1, 'age': col2,
                            'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus", color="age", title="age")
        return fig

    ################################################################   100<NAV<500  ###############################################
    def segmentation2(self):
        col0 = ['cluster0', 'cluster1', 'cluster2', 'cluster3']
        col1 = [8581, 53197, 31731, 21466]
        fig = go.Figure(
            data=[go.Pie(labels=col0, values=col1, pull=[0, 0, 0.2, 0])])
        return fig.update_layout(
            title='Clusters'), len(col0)

    def loan_value_average2(self):
        colx = 'cluster'
        coly = 'Loan value average (ty VND)'
        df0 = self.gen(0, 0, 0, 0, 0, 0, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 0.049, 0.003, 0.07, 0.063, 0.01, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 0.082, 0.0148, 0.0148, 0.109, 0.01, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(0, 0, 0, 0, 0, 0, coly)
        df3['cluster'] = 'cluster3'

        return self.boxplot(colx, coly, df0, df1, df2, df3).update_layout(
            title='Loan value average')

    def der_transaction_value_average2(self):

        col0 = ['cluster0']*2+['cluster1']*2+['cluster2']*2+['cluster3']*2
        col1 = ['zero', 'not zero']*4
        col2 = [98.1, 100-98.1, 93.7, 100-93.7, 91.8, 100-91.8, 96.5, 100-96.5]
        data = pd.DataFrame(
            {'cluster': col0, 'zero or not': col1, 'percent': col2})
        fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'domain'}, {
                            'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]])
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster0']['zero or not'], values=data[data['cluster'] == 'cluster0']['percent'], name="cluster0", marker_colors=self.night_colors),
                      1, 1)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster1']['zero or not'], values=data[data['cluster'] == 'cluster1']['percent'], name="cluster1", marker_colors=self.sunflowers_colors),
                      1, 2)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster2']['zero or not'], values=data[data['cluster'] == 'cluster2']['percent'], name="cluster2", marker_colors=self.irises_colors),
                      2, 1)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster3']['zero or not'], values=data[data['cluster'] == 'cluster3']['percent'], name="cluster3", marker_colors=self.cafe_colors),
                      2, 2)

        fig.update_traces(hole=.4, hoverinfo="label+percent+name")
        fig.update_layout(
            title_text="der transaction value average",
            annotations=[dict(text='cluster0', x=0.19, y=0.82, font_size=13, showarrow=False),
                         dict(text='cluster1', x=0.81, y=0.82,
                              font_size=13, showarrow=False),
                         dict(text='cluster2', x=0.19, y=0.19,
                              font_size=13, showarrow=False),
                         dict(text='cluster3', x=0.81, y=0.19, font_size=13, showarrow=False)])
        fig = go.Figure(fig)
        return fig.update_layout(
            title='Der transaction value average')

    def Stock_total_order_average2(self):
        colx = 'cluster'
        coly = 'Stock total order average'
        df0 = self.gen(5, 2.7, 0, 1.167, 4.5, 1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(5, 6.3, 2.83, 5.5, 9, 1, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(5, 7.2, 3.5, 6.5, 10.167, 1, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(5, 4.9, 2, 4.167, 7.167, 1, coly)
        df3['cluster'] = 'cluster3'
        fig = self.boxplot(colx, coly, df0, df1, df2, df3)
        return fig

    def Stock_transaction_value_average2(self):
        colx = 'cluster'
        coly = 'Stock transaction value average (ty VND)'
        df0 = self.gen(2, 0.587, 0.1, 0.165, 0.676, 0.1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 2.69, 0.574, 1.35, 3.1, 1, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 3.7, 1, 2.15, 4.45, 1, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(2, 1.18, 0.325, 0.6867, 1.4, 1, coly)
        df3['cluster'] = 'cluster3'

        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def NAV2(self):
        colx = 'cluster'
        coly = 'NAV (ty VND)'
        df0 = self.gen(2, 0.2306, 0.1362, 0.2043, 0.3085, 0.1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 0.2335, 0.141, 0.2055, 0.3082, 0.1, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 0.2422, 0.1475, 0.2157, 0.322, 0.1, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(2, 0.2207, 0.133, 0.1925, 0.2875, 0.1, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def time_open2(self):
        colx = 'cluster'
        coly = 'Time open (ty VND)'
        df0 = self.gen(2, 360, 154, 226, 415, 100, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 289, 164, 231, 339, 100, coly)
        df1['cluster'] = 'cluster1'
        df2 = self.gen(2, 308, 171, 248, 359, 100, coly)
        df2['cluster'] = 'cluster2'
        df3 = self.gen(2, 261, 142, 210, 315, 100, coly)
        df3['cluster'] = 'cluster3'
        return self.boxplot(colx, coly, df0, df1, df2, df3)

    def city_of_star2(self):
        col1 = ['cluster0']*4+['cluster1']*4+['cluster2']*4+['cluster3']*4
        col2 = ['HN', 'HCM', 'Others', 'DSVN']*4
        col3 = [45.6, 10.5, 7.6, 7, 39.1, 14.8, 8,
                7.5, 36.3, 16, 7.6, 8, 43.3, 13, 8, 7.4]
        col4 = [8581]*4+[53197]*4+[31731]*4+[21466]*4
        data = pd.DataFrame({'cluster': col1, 'city': col2,
                            'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="city", title="City of Star")
        return fig

    def business2(self):
        col1 = ['cluster0']*4+['cluster1']*2+['cluster2']*2+['cluster3']
        col2 = ['TVDT', 'DVKH', 'TVTC', 'DOI TAC']+['TVDT', 'DVKH']*2+['TVDT']
        col3 = [2.2, 39.2, 45.2, 13.4, 96.4, 3, 93.9, 5, 100]
        col4 = [8581]*4+[53197]*2+[31731]*2+[21466]
        data = pd.DataFrame(
            {'cluster': col1, 'Business party': col2, 'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="Business party", title="Business")
        return fig

    def product2(self):

        col1 = ['cluster0']*3+['cluster1']*2+['cluster2']*2+['cluster3']*2
        col2 = ['1', '2', '3']+['1', '3']*3
        col3 = [48.4, 41.6, 10.1, 97.6, 2.3, 98.3, 1.7, 96.6, 3.4]
        col4 = [8581]*3+[53197]*2+[31731]*2+[21466]*2
        data = pd.DataFrame(
            {'cluster': col1, 'product status': col2, 'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="product status", title="product")
        return fig

    def age2(self):
        col1 = ['cluster0']*6+['cluster1']*6+['cluster2']*6+['cluster3']*6
        col2 = [1, 2, 3, 4, 5, 6]*4
        col3 = [1.3, 3.5, 19, 41.2, 15.5, 19.5, 1.7, 4.3, 22.3, 4.5, 1.8,
                4.5, 22.7, 52.2, 13.9, 5, 1.5, 4.1, 21.6, 31.6, 15.6, 5.4, 3.8, 2.2]
        col4 = [8581]*6+[53197]*6+[31731]*6+[21466]*6
        data = pd.DataFrame({'cluster': col1, 'age': col2,
                            'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus", color="age", title="age")
        return fig

    #######################################################################  100 > NAV #########################################################################################
    def segmentation3(self):
        col0 = ['cluster0', 'cluster1']
        col1 = [80484, 21975]
        fig = go.Figure(
            data=[go.Pie(labels=col0, values=col1, pull=[0, 0, 0.2, 0])])
        return fig.update_layout(
            title='Clusters'), len(col0)

    def loan_value_average3(self):
        colx = 'cluster'
        coly = 'Loan value average (ty VND)'
        df0 = self.gen(2, 12, 0, 0, 4.8, 2, coly)
        df0['cluster'] = 'cluster0'
        df3 = self.gen(2, 0, 0, 0, 0, 1, coly)
        df3['cluster'] = 'cluster1'
        return self.boxplot(colx, coly, df0, df3).update_layout(
            title='Loan value average')

    def der_transaction_value_average3(self):

        col0 = ['cluster0']*2+['cluster1']*2
        col1 = ['zero', 'not zero']*2
        col2 = [95, 100-95, 97.6, 100-97.6]
        data = pd.DataFrame(
            {'cluster': col0, 'zero or not': col1, 'percent': col2})
        fig = make_subplots(rows=1, cols=2, specs=[
                            [{'type': 'domain'}, {'type': 'domain'}]])
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster0']['zero or not'], values=data[data['cluster'] == 'cluster0']['percent'], name="cluster0", marker_colors=self.night_colors),
                      1, 1)
        fig.add_trace(go.Pie(labels=data[data['cluster'] == 'cluster1']['zero or not'], values=data[data['cluster'] == 'cluster1']['percent'], name="cluster1", marker_colors=self.sunflowers_colors),
                      1, 2)

        fig.update_traces(hole=.4, hoverinfo="label+percent+name")
        fig.update_layout(
            title_text="der transaction value average",
            annotations=[dict(text='cluster0', x=0.18, y=0.5, font_size=20, showarrow=False),
                         dict(text='cluster1', x=0.82, y=0.5, font_size=20, showarrow=False)])
        fig = go.Figure(fig)
        return fig.update_layout(
            title='Der transaction value average')

    def Stock_total_order_average3(self):
        df0 = self.gen(3, 3.2, 0.83, 2.167, 4.5, 1,
                       'Stock total order average')
        df0['cluster'] = 'cluster0'
        df1 = self.gen(3, 2.1, 0.33, 1.33, 3, 1, 'Stock total order average')
        df1['cluster'] = 'cluster1'
        df = pd.concat([df0, df1], ignore_index=True, axis=0)
        fig = px.box(df, x='cluster', y='Stock total order average')
        return fig

    def Stock_transaction_value_average3(self):
        colx = 'cluster'
        coly = 'Stock transaction value average (ty VND)'
        df0 = self.gen(2, 0.687, 0.0397, 0.143, 0.466, 0.5, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 0.255, 0.0076, 0.047, 0.172, 0.5, coly)
        df1['cluster'] = 'cluster1'
        return self.boxplot(colx, coly, df0, df1)

    def NAV3(self):
        colx = 'cluster'
        coly = 'NAV (ty VND)'
        df0 = self.gen(2, 0.0326, 0.0062, 0.0248, 0.0525, 0.1, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 0.0265, 0.003, 0.0165, 0.0442, 0.1, coly)
        df1['cluster'] = 'cluster1'
        return self.boxplot(colx, coly, df0, df1)

    def time_open3(self):
        colx = 'cluster'
        coly = 'Time open (ty VND)'
        df0 = self.gen(2, 238, 125, 183, 283, 100, coly)
        df0['cluster'] = 'cluster0'
        df1 = self.gen(2, 221, 105, 168, 241, 100, coly)
        df1['cluster'] = 'cluster1'
        return self.boxplot(colx, coly, df0, df1)

    def city_of_star3(self):
        col1 = ['cluster0']*4+['cluster1']*4
        col2 = ['HN', 'HCM', 'Others', 'DSVN']*2
        col3 = [33, 13.8, 10.1, 8.9, 33.3, 11.2, 13.7, 11]
        col4 = [80484]*4+[21975]*4
        data = pd.DataFrame({'cluster': col1, 'city': col2,
                            'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="city", title="City of Star")
        return fig

    def business3(self):
        col1 = ['cluster0']*1+['cluster1']*3
        col2 = ['TVDT', 'DVKH', 'TVTC', 'DOI TAC']
        col3 = [99.5, 69, 23, 8]
        col4 = [80484]+[21975]*3
        data = pd.DataFrame(
            {'cluster': col1, 'Business party': col2, 'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="Business party", title="Business")
        return fig

    def product3(self):

        col1 = ['cluster0']*3+['cluster1']*3
        col2 = ['1', '2', '3']*2
        col3 = [98.9, 0.2, 0.9, 84.2, 12.5, 3.2]
        col4 = [80484]*3+[21975]*3
        data = pd.DataFrame(
            {'cluster': col1, 'product status': col2, 'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus",
                     color="product status", title="product")
        return fig

    def age3(self):
        col1 = ['cluster0']*6+['cluster1']*6
        col2 = [1, 2, 3, 4, 5, 6]*2
        col3 = [6.2, 11.6, 28.7, 41.8, 8.5, 2.9, 8, 13.1, 32.2, 35.1, 7, 4.6]
        col4 = [80484]*6+[21975]*6
        data = pd.DataFrame({'cluster': col1, 'age': col2,
                            'top percent': col3, 'sample': col4})
        data['No Cus'] = (data['top percent']*data['sample'] /
                          100).apply(lambda x: round(x, 0))
        fig = px.bar(data, x="cluster", y="No Cus", color="age", title="age")
        return fig

    @staticmethod
    def gen(k, mean, q25, q50, q75, eps, col):
        data = [q25]*k + [q50]*k + [q75]*k
        m3 = (len(data)+2)*mean-sum(data)
        x = min([m3-q25, q25])
        a = x-eps
        b = m3-a
        data += [a, b]
        return pd.DataFrame(data, columns=[col])

    @staticmethod
    def boxplot(colx, coly, *arg):
        data = pd.concat([df for df in arg], ignore_index=True, axis=0)
        cls = data.cluster.unique()
        fig = go.Figure()
        for cluster in cls:
            fig.add_trace(
                go.Box(y=data[data['cluster'] == cluster][coly], name=cluster))

        return fig


def table_df():

    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    return df.to_dict('records')


app = Dash(__name__)
# ======================== App Layout
app.layout = html.Div([
    html.H1('Customer Profiling Dashboard', style={
            'text-align': 'center', 'background-color': '#7DF9FF', 'font-family': 'Sans-serif'}),
    html.P("""Select clustering strategy:""",
           style={'margin-right': '2em', 'verticalAlign': "middle", 'font-weight': '700',
                  'font-family': 'Sans-serif', 'fontSize': "25px"}),
    dcc.Dropdown(
        id='strategy_area_dropdown',
        options=[
            {'label': 'NAV > 500M', 'value': 'nav_>_500'},
            {'label': '100M < NAV <= 500M', 'value': '100<nav<=500'},
            {'label': 'NAV <= 100M', 'value': 'nav_<=_100M'}
        ],
        value='nav_>_500',
        placeholder="Select Strategy",
        style=dict(
            width='40%',
            verticalAlign="middle"
        )
    ),
    html.P("""Clustering Result""",
           style={'margin-right': '2em', 'verticalAlign': "middle", 'font-weight': '700',
                  'font-family': 'Sans-serif', 'fontSize': "25px"}),
    html.H4(id="count_segment", style={'width': '40%',
                                       'height': '2vh', 'display': 'outline-block'}),

    html.Div(dcc.Graph(id="segmentation", figure={}, style={
        "width": "100%",
        "height": "100%"
    }),
        style={
        "width": "100%",
        "height": "100%",
    },
    ),
    html.H4("""Custormers Info""", style={'width': '40%',
                                          'height': '2vh', 'display': 'outline-block'}),
    dash_table.DataTable(data=[], id='table', style_table={
        'width': '50%', 'height': '40vh', 'display': 'inline-block'}),
    html.H4("""Clustering Characteristics""", style={'width': '40%',
                                                     'height': '2vh', 'display': 'outline-block'}),
    dcc.Graph(id="loan_value_average", figure={}, style={'width': '50%',
              'height': '40vh', 'display': 'inline-block'}),
    dcc.Graph(id="der_transaction_value_average", figure={}, style={'width': '50%',
              'height': '40vh', 'display': 'inline-block'}),
    dcc.Graph(id="Stock_total_order_average", figure={}, style={'width': '50%',
              'height': '40vh', 'display': 'inline-block'}),
    dcc.Graph(id="Stock_transaction_value_average", figure={}, style={
              'width': '50%', 'height': '40vh', 'display': 'inline-block'}),
    dcc.Graph(id="NAV", figure={}, style={'width': '50%', 'height': '40vh',
              'display': 'inline-block'}),
    dcc.Graph(id="time_open", figure={}, style={'width': '50%', 'height': '40vh',
              'display': 'inline-block'}),
    dcc.Graph(id="city_of_star", figure={}, style={'width': '50%', 'height': '40vh',
              'display': 'inline-block'}),
    dcc.Graph(id="business", figure={}, style={'width': '50%', 'height': '40vh',
              'display': 'inline-block'}),
    dcc.Graph(id="product", figure={}, style={'width': '50%', 'height': '40vh',
              'display': 'inline-block'}),
    dcc.Graph(id="age", figure={}, style={'width': '50%', 'height': '40vh',
              'display': 'inline-block'}),
    dcc.Textarea(
        id='textarea-example',
        value="""
        0: Total products are active \n
        1: Stock or Derivative is active and Bond or MM or Deposit is inactive \n
        2: Stock or Derivative is active and Bond or MM or Deposit is active \n
        3: Others
        """,
        style={'width': '50%', 'height': 130},
    )
])


@app.callback(
    [
        Output("count_segment", component_property='children'),
        Output("segmentation", "figure"),
        Output("table", "data"),
        Output("loan_value_average", "figure"),
        Output("der_transaction_value_average", "figure"),
        Output("Stock_total_order_average", "figure"),
        Output("Stock_transaction_value_average", "figure"),
        Output("NAV", "figure"),
        Output("time_open", "figure"),
        Output("city_of_star", "figure"),
        Output("business", "figure"),
        Output("product", "figure"),
        Output("age", "figure"),
    ],
    Input('strategy_area_dropdown', 'value')
)
def update_output(value):
    graphs = []
    if value == 'nav_>_500':
        g1, g0 = dashboard().segmentation1()
        graphs = [
            g1,
            table_df(),
            dashboard().loan_value_average1(),
            dashboard().der_transaction_value_average1(),
            dashboard().Stock_total_order_average1(),
            dashboard().Stock_transaction_value_average1(),
            dashboard().NAV1(),
            dashboard().time_open1(),
            dashboard().city_of_star1(),
            dashboard().business1(),
            dashboard().product1(),
            dashboard().age1()]
    elif value == '100<nav<=500':
        g1, g0 = dashboard().segmentation2()
        graphs = [
            g1,
            table_df(),
            dashboard().loan_value_average2(),
            dashboard().der_transaction_value_average2(),
            dashboard().Stock_total_order_average2(),
            dashboard().Stock_transaction_value_average2(),
            dashboard().NAV2(),
            dashboard().time_open2(),
            dashboard().city_of_star2(),
            dashboard().business2(),
            dashboard().product2(),
            dashboard().age2()]
    elif value == 'nav_<=_100M':
        g1, g0 = dashboard().segmentation3()
        graphs = [
            g1,
            table_df(),
            dashboard().loan_value_average3(),
            dashboard().der_transaction_value_average3(),
            dashboard().Stock_total_order_average3(),
            dashboard().Stock_transaction_value_average3(),
            dashboard().NAV3(),
            dashboard().time_open3(),
            dashboard().city_of_star3(),
            dashboard().business3(),
            dashboard().product3(),
            dashboard().age3()]

    g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12 = graphs
    g0 = f'Number clusters found: {g0}'
    return g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, dev_tools_hot_reload=True)
