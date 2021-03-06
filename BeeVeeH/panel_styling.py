import wx

class StylingPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.SetBackgroundColour('#ededed')

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # self.connector_style_select = wx.ComboBox(self, -1, choices=['Line', 'Hidden'])
        self.connector_thickness_slider = wx.Slider(self, -1, 2, 0, 30,
                style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.joint_radius_slider = wx.Slider(self, -1, 2, 0, 30,
                style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.head_double_size_checkbox = wx.CheckBox(self, -1, 'Head double size')
        self.head_double_size_checkbox.SetValue(True)
        self.sculpture_mode_checkbox = wx.CheckBox(self, -1, 'Sculpture mode, interval: ')
        self.sculpture_mode_checkbox.SetValue(False)
        self.sculpture_interval_entry = wx.TextCtrl(self, -1, size=(40, -1))
        self.sculpture_interval_entry.SetValue('3')


        hbox.AddSpacer(10)
        # hbox.Add(wx.StaticText(self, -1, 'Connector style: '), 0, wx.ALIGN_CENTER)
        # hbox.Add(self.connector_style_select, 0, wx.ALIGN_CENTER)
        # hbox.AddSpacer(10)
        hbox.Add(wx.StaticText(self, -1, 'Connector thinkness: '), 0, wx.ALIGN_CENTER)
        hbox.Add(self.connector_thickness_slider, 1, wx.EXPAND)
        hbox.AddSpacer(10)
        hbox.Add(wx.StaticText(self, -1, 'Joint radius: '), 0, wx.ALIGN_CENTER)
        hbox.Add(self.joint_radius_slider, 1, wx.EXPAND)
        hbox.AddSpacer(10)
        hbox.Add(self.head_double_size_checkbox, 0, wx.ALIGN_CENTER)
        hbox.AddSpacer(10)
        hbox.Add(self.sculpture_mode_checkbox, 0, wx.ALIGN_CENTER)
        hbox.Add(self.sculpture_interval_entry, 0, wx.ALIGN_CENTER)
        hbox.AddSpacer(10)


        self.SetSizer(hbox)

    def bind_events(self,
                    OnConnectorThinknessChanged,
                    OnJointRadiusChanged,
                    OnHeadJointDoubleSizeChanged,
                    OnSculptureModeChanged,
                    OnSculptureIntervalChanged):
        self.connector_thickness_slider.Bind(wx.EVT_SLIDER, OnConnectorThinknessChanged)
        self.joint_radius_slider.Bind(wx.EVT_SLIDER, OnJointRadiusChanged)
        self.head_double_size_checkbox.Bind(wx.EVT_CHECKBOX, OnHeadJointDoubleSizeChanged)
        self.sculpture_mode_checkbox.Bind(wx.EVT_CHECKBOX, OnSculptureModeChanged)
        self.sculpture_interval_entry.Bind(wx.EVT_TEXT, OnSculptureIntervalChanged)

