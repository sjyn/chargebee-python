import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Subscription(Model):
    class Addon(Model):
      fields = ["id", "quantity", "unit_price", "amount", "trial_end", "remaining_billing_cycles", "quantity_in_decimal", "unit_price_in_decimal", "amount_in_decimal"]
      pass
    class EventBasedAddon(Model):
      fields = ["id", "quantity", "unit_price", "service_period_in_days", "on_event", "charge_once", "quantity_in_decimal", "unit_price_in_decimal"]
      pass
    class ChargedEventBasedAddon(Model):
      fields = ["id", "last_charged_at"]
      pass
    class Coupon(Model):
      fields = ["coupon_id", "apply_till", "applied_count", "coupon_code"]
      pass
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass
    class ReferralInfo(Model):
      fields = ["referral_code", "coupon_code", "referrer_id", "external_reference_id", "reward_status", "referral_system", "account_id", "campaign_id", "external_campaign_id", "friend_offer_type", "referrer_reward_type", "notify_referral_system", "destination_url", "post_purchase_widget_enabled"]
      pass
    class ContractTerm(Model):
      fields = ["id", "status", "contract_start", "contract_end", "billing_cycle", "action_at_term_end", "total_contract_value", "cancellation_cutoff_period", "created_at", "subscription_id", "remaining_billing_cycles"]
      pass

    fields = ["id", "currency_code", "plan_id", "plan_quantity", "plan_unit_price", "setup_fee", \
    "billing_period", "billing_period_unit", "start_date", "trial_end", "remaining_billing_cycles", \
    "po_number", "auto_collection", "customer_id", "plan_amount", "plan_free_quantity", "status", \
    "trial_start", "current_term_start", "current_term_end", "next_billing_at", "created_at", "started_at", \
    "activated_at", "gift_id", "contract_term_billing_cycle_on_renewal", "override_relationship", \
    "pause_date", "resume_date", "cancelled_at", "cancel_reason", "affiliate_token", "created_from_ip", \
    "resource_version", "updated_at", "has_scheduled_changes", "payment_source_id", "plan_free_quantity_in_decimal", \
    "plan_quantity_in_decimal", "plan_unit_price_in_decimal", "plan_amount_in_decimal", "offline_payment_method", \
    "due_invoices_count", "due_since", "total_dues", "mrr", "exchange_rate", "base_currency_code", \
    "addons", "event_based_addons", "charged_event_based_addons", "coupon", "coupons", "shipping_address", \
    "referral_info", "invoice_notes", "meta_data", "deleted", "contract_term", "cancel_reason_code", \
    "free_period", "free_period_unit"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions"), params, env, headers)

    @staticmethod
    def create_for_customer(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"subscriptions"), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("subscriptions"), params, env, headers)

    @staticmethod
    def subscriptions_for_customer(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("customers",id,"subscriptions"), params, env, headers)

    @staticmethod
    def contract_terms_for_subscription(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"contract_terms"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id), None, env, headers)

    @staticmethod
    def retrieve_with_scheduled_changes(id, env=None, headers=None):
        return request.send('get', request.uri_path("subscriptions",id,"retrieve_with_scheduled_changes"), None, env, headers)

    @staticmethod
    def remove_scheduled_changes(id, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_changes"), None, env, headers)

    @staticmethod
    def remove_scheduled_cancellation(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_cancellation"), params, env, headers)

    @staticmethod
    def remove_coupons(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_coupons"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id), params, env, headers)

    @staticmethod
    def change_term_end(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"change_term_end"), params, env, headers)

    @staticmethod
    def reactivate(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"reactivate"), params, env, headers)

    @staticmethod
    def add_charge_at_term_end(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"add_charge_at_term_end"), params, env, headers)

    @staticmethod
    def charge_addon_at_term_end(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"charge_addon_at_term_end"), params, env, headers)

    @staticmethod
    def charge_future_renewals(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"charge_future_renewals"), params, env, headers)

    @staticmethod
    def import_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions","import_subscription"), params, env, headers)

    @staticmethod
    def import_for_customer(id, params, env=None, headers=None):
        return request.send('post', request.uri_path("customers",id,"import_subscription"), params, env, headers)

    @staticmethod
    def import_contract_term(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"import_contract_term"), params, env, headers)

    @staticmethod
    def override_billing_profile(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"override_billing_profile"), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"delete"), None, env, headers)

    @staticmethod
    def pause(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"pause"), params, env, headers)

    @staticmethod
    def cancel(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"cancel"), params, env, headers)

    @staticmethod
    def resume(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"resume"), params, env, headers)

    @staticmethod
    def remove_scheduled_pause(id, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_pause"), None, env, headers)

    @staticmethod
    def remove_scheduled_resumption(id, env=None, headers=None):
        return request.send('post', request.uri_path("subscriptions",id,"remove_scheduled_resumption"), None, env, headers)
