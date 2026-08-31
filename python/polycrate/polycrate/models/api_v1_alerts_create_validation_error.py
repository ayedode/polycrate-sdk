from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_create_alert_router_error_component import ApiV1AlertsCreateAlertRouterErrorComponent
    from ..models.api_v1_alerts_create_annotations_error_component import ApiV1AlertsCreateAnnotationsErrorComponent
    from ..models.api_v1_alerts_create_archived_at_error_component import ApiV1AlertsCreateArchivedAtErrorComponent
    from ..models.api_v1_alerts_create_archived_error_component import ApiV1AlertsCreateArchivedErrorComponent
    from ..models.api_v1_alerts_create_archived_reason_error_component import (
        ApiV1AlertsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alerts_create_block_error_component import ApiV1AlertsCreateBlockErrorComponent
    from ..models.api_v1_alerts_create_category_error_component import ApiV1AlertsCreateCategoryErrorComponent
    from ..models.api_v1_alerts_create_criticality_error_component import ApiV1AlertsCreateCriticalityErrorComponent
    from ..models.api_v1_alerts_create_dashboard_url_error_component import ApiV1AlertsCreateDashboardUrlErrorComponent
    from ..models.api_v1_alerts_create_debug_mode_error_component import ApiV1AlertsCreateDebugModeErrorComponent
    from ..models.api_v1_alerts_create_display_name_error_component import ApiV1AlertsCreateDisplayNameErrorComponent
    from ..models.api_v1_alerts_create_external_url_error_component import ApiV1AlertsCreateExternalUrlErrorComponent
    from ..models.api_v1_alerts_create_fingerprint_error_component import ApiV1AlertsCreateFingerprintErrorComponent
    from ..models.api_v1_alerts_create_generator_url_error_component import ApiV1AlertsCreateGeneratorUrlErrorComponent
    from ..models.api_v1_alerts_create_k8s_app_error_component import ApiV1AlertsCreateK8SAppErrorComponent
    from ..models.api_v1_alerts_create_k8s_cluster_error_component import ApiV1AlertsCreateK8SClusterErrorComponent
    from ..models.api_v1_alerts_create_kind_error_component import ApiV1AlertsCreateKindErrorComponent
    from ..models.api_v1_alerts_create_labels_error_component import ApiV1AlertsCreateLabelsErrorComponent
    from ..models.api_v1_alerts_create_last_seen_error_component import ApiV1AlertsCreateLastSeenErrorComponent
    from ..models.api_v1_alerts_create_message_error_component import ApiV1AlertsCreateMessageErrorComponent
    from ..models.api_v1_alerts_create_name_error_component import ApiV1AlertsCreateNameErrorComponent
    from ..models.api_v1_alerts_create_namespace_error_component import ApiV1AlertsCreateNamespaceErrorComponent
    from ..models.api_v1_alerts_create_non_field_errors_error_component import (
        ApiV1AlertsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alerts_create_panel_url_error_component import ApiV1AlertsCreatePanelUrlErrorComponent
    from ..models.api_v1_alerts_create_platform_service_error_component import (
        ApiV1AlertsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alerts_create_pod_error_component import ApiV1AlertsCreatePodErrorComponent
    from ..models.api_v1_alerts_create_provider_error_component import ApiV1AlertsCreateProviderErrorComponent
    from ..models.api_v1_alerts_create_provider_id_error_component import ApiV1AlertsCreateProviderIdErrorComponent
    from ..models.api_v1_alerts_create_provider_reference_error_component import (
        ApiV1AlertsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alerts_create_reconciliation_enabled_error_component import (
        ApiV1AlertsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alerts_create_silence_ends_at_error_component import (
        ApiV1AlertsCreateSilenceEndsAtErrorComponent,
    )
    from ..models.api_v1_alerts_create_silence_url_error_component import ApiV1AlertsCreateSilenceUrlErrorComponent
    from ..models.api_v1_alerts_create_sla_availability_error_component import (
        ApiV1AlertsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_create_sla_target_error_component import ApiV1AlertsCreateSlaTargetErrorComponent
    from ..models.api_v1_alerts_create_slo_availability_error_component import (
        ApiV1AlertsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_create_slo_target_error_component import ApiV1AlertsCreateSloTargetErrorComponent
    from ..models.api_v1_alerts_create_status_error_component import ApiV1AlertsCreateStatusErrorComponent
    from ..models.api_v1_alerts_create_suppressed_error_component import ApiV1AlertsCreateSuppressedErrorComponent
    from ..models.api_v1_alerts_create_target_availability_error_component import (
        ApiV1AlertsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_create_title_error_component import ApiV1AlertsCreateTitleErrorComponent
    from ..models.api_v1_alerts_create_tolerations_error_component import ApiV1AlertsCreateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1AlertsCreateValidationError")


@_attrs_define
class ApiV1AlertsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsCreateAlertRouterErrorComponent | ApiV1AlertsCreateAnnotationsErrorComponent |
            ApiV1AlertsCreateArchivedAtErrorComponent | ApiV1AlertsCreateArchivedErrorComponent |
            ApiV1AlertsCreateArchivedReasonErrorComponent | ApiV1AlertsCreateBlockErrorComponent |
            ApiV1AlertsCreateCategoryErrorComponent | ApiV1AlertsCreateCriticalityErrorComponent |
            ApiV1AlertsCreateDashboardUrlErrorComponent | ApiV1AlertsCreateDebugModeErrorComponent |
            ApiV1AlertsCreateDisplayNameErrorComponent | ApiV1AlertsCreateExternalUrlErrorComponent |
            ApiV1AlertsCreateFingerprintErrorComponent | ApiV1AlertsCreateGeneratorUrlErrorComponent |
            ApiV1AlertsCreateK8SAppErrorComponent | ApiV1AlertsCreateK8SClusterErrorComponent |
            ApiV1AlertsCreateKindErrorComponent | ApiV1AlertsCreateLabelsErrorComponent |
            ApiV1AlertsCreateLastSeenErrorComponent | ApiV1AlertsCreateMessageErrorComponent |
            ApiV1AlertsCreateNameErrorComponent | ApiV1AlertsCreateNamespaceErrorComponent |
            ApiV1AlertsCreateNonFieldErrorsErrorComponent | ApiV1AlertsCreatePanelUrlErrorComponent |
            ApiV1AlertsCreatePlatformServiceErrorComponent | ApiV1AlertsCreatePodErrorComponent |
            ApiV1AlertsCreateProviderErrorComponent | ApiV1AlertsCreateProviderIdErrorComponent |
            ApiV1AlertsCreateProviderReferenceErrorComponent | ApiV1AlertsCreateReconciliationEnabledErrorComponent |
            ApiV1AlertsCreateSilenceEndsAtErrorComponent | ApiV1AlertsCreateSilenceUrlErrorComponent |
            ApiV1AlertsCreateSlaAvailabilityErrorComponent | ApiV1AlertsCreateSlaTargetErrorComponent |
            ApiV1AlertsCreateSloAvailabilityErrorComponent | ApiV1AlertsCreateSloTargetErrorComponent |
            ApiV1AlertsCreateStatusErrorComponent | ApiV1AlertsCreateSuppressedErrorComponent |
            ApiV1AlertsCreateTargetAvailabilityErrorComponent | ApiV1AlertsCreateTitleErrorComponent |
            ApiV1AlertsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsCreateAlertRouterErrorComponent
        | ApiV1AlertsCreateAnnotationsErrorComponent
        | ApiV1AlertsCreateArchivedAtErrorComponent
        | ApiV1AlertsCreateArchivedErrorComponent
        | ApiV1AlertsCreateArchivedReasonErrorComponent
        | ApiV1AlertsCreateBlockErrorComponent
        | ApiV1AlertsCreateCategoryErrorComponent
        | ApiV1AlertsCreateCriticalityErrorComponent
        | ApiV1AlertsCreateDashboardUrlErrorComponent
        | ApiV1AlertsCreateDebugModeErrorComponent
        | ApiV1AlertsCreateDisplayNameErrorComponent
        | ApiV1AlertsCreateExternalUrlErrorComponent
        | ApiV1AlertsCreateFingerprintErrorComponent
        | ApiV1AlertsCreateGeneratorUrlErrorComponent
        | ApiV1AlertsCreateK8SAppErrorComponent
        | ApiV1AlertsCreateK8SClusterErrorComponent
        | ApiV1AlertsCreateKindErrorComponent
        | ApiV1AlertsCreateLabelsErrorComponent
        | ApiV1AlertsCreateLastSeenErrorComponent
        | ApiV1AlertsCreateMessageErrorComponent
        | ApiV1AlertsCreateNameErrorComponent
        | ApiV1AlertsCreateNamespaceErrorComponent
        | ApiV1AlertsCreateNonFieldErrorsErrorComponent
        | ApiV1AlertsCreatePanelUrlErrorComponent
        | ApiV1AlertsCreatePlatformServiceErrorComponent
        | ApiV1AlertsCreatePodErrorComponent
        | ApiV1AlertsCreateProviderErrorComponent
        | ApiV1AlertsCreateProviderIdErrorComponent
        | ApiV1AlertsCreateProviderReferenceErrorComponent
        | ApiV1AlertsCreateReconciliationEnabledErrorComponent
        | ApiV1AlertsCreateSilenceEndsAtErrorComponent
        | ApiV1AlertsCreateSilenceUrlErrorComponent
        | ApiV1AlertsCreateSlaAvailabilityErrorComponent
        | ApiV1AlertsCreateSlaTargetErrorComponent
        | ApiV1AlertsCreateSloAvailabilityErrorComponent
        | ApiV1AlertsCreateSloTargetErrorComponent
        | ApiV1AlertsCreateStatusErrorComponent
        | ApiV1AlertsCreateSuppressedErrorComponent
        | ApiV1AlertsCreateTargetAvailabilityErrorComponent
        | ApiV1AlertsCreateTitleErrorComponent
        | ApiV1AlertsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_create_alert_router_error_component import (
            ApiV1AlertsCreateAlertRouterErrorComponent,
        )
        from ..models.api_v1_alerts_create_annotations_error_component import ApiV1AlertsCreateAnnotationsErrorComponent
        from ..models.api_v1_alerts_create_archived_at_error_component import ApiV1AlertsCreateArchivedAtErrorComponent
        from ..models.api_v1_alerts_create_archived_error_component import ApiV1AlertsCreateArchivedErrorComponent
        from ..models.api_v1_alerts_create_archived_reason_error_component import (
            ApiV1AlertsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alerts_create_category_error_component import ApiV1AlertsCreateCategoryErrorComponent
        from ..models.api_v1_alerts_create_criticality_error_component import ApiV1AlertsCreateCriticalityErrorComponent
        from ..models.api_v1_alerts_create_dashboard_url_error_component import (
            ApiV1AlertsCreateDashboardUrlErrorComponent,
        )
        from ..models.api_v1_alerts_create_debug_mode_error_component import ApiV1AlertsCreateDebugModeErrorComponent
        from ..models.api_v1_alerts_create_display_name_error_component import (
            ApiV1AlertsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alerts_create_external_url_error_component import (
            ApiV1AlertsCreateExternalUrlErrorComponent,
        )
        from ..models.api_v1_alerts_create_fingerprint_error_component import ApiV1AlertsCreateFingerprintErrorComponent
        from ..models.api_v1_alerts_create_generator_url_error_component import (
            ApiV1AlertsCreateGeneratorUrlErrorComponent,
        )
        from ..models.api_v1_alerts_create_k8s_app_error_component import ApiV1AlertsCreateK8SAppErrorComponent
        from ..models.api_v1_alerts_create_k8s_cluster_error_component import ApiV1AlertsCreateK8SClusterErrorComponent
        from ..models.api_v1_alerts_create_kind_error_component import ApiV1AlertsCreateKindErrorComponent
        from ..models.api_v1_alerts_create_labels_error_component import ApiV1AlertsCreateLabelsErrorComponent
        from ..models.api_v1_alerts_create_last_seen_error_component import ApiV1AlertsCreateLastSeenErrorComponent
        from ..models.api_v1_alerts_create_message_error_component import ApiV1AlertsCreateMessageErrorComponent
        from ..models.api_v1_alerts_create_name_error_component import ApiV1AlertsCreateNameErrorComponent
        from ..models.api_v1_alerts_create_namespace_error_component import ApiV1AlertsCreateNamespaceErrorComponent
        from ..models.api_v1_alerts_create_non_field_errors_error_component import (
            ApiV1AlertsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alerts_create_panel_url_error_component import ApiV1AlertsCreatePanelUrlErrorComponent
        from ..models.api_v1_alerts_create_platform_service_error_component import (
            ApiV1AlertsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alerts_create_pod_error_component import ApiV1AlertsCreatePodErrorComponent
        from ..models.api_v1_alerts_create_provider_error_component import ApiV1AlertsCreateProviderErrorComponent
        from ..models.api_v1_alerts_create_provider_id_error_component import ApiV1AlertsCreateProviderIdErrorComponent
        from ..models.api_v1_alerts_create_provider_reference_error_component import (
            ApiV1AlertsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alerts_create_reconciliation_enabled_error_component import (
            ApiV1AlertsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alerts_create_silence_ends_at_error_component import (
            ApiV1AlertsCreateSilenceEndsAtErrorComponent,
        )
        from ..models.api_v1_alerts_create_silence_url_error_component import ApiV1AlertsCreateSilenceUrlErrorComponent
        from ..models.api_v1_alerts_create_sla_availability_error_component import (
            ApiV1AlertsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_create_sla_target_error_component import ApiV1AlertsCreateSlaTargetErrorComponent
        from ..models.api_v1_alerts_create_slo_availability_error_component import (
            ApiV1AlertsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_create_slo_target_error_component import ApiV1AlertsCreateSloTargetErrorComponent
        from ..models.api_v1_alerts_create_status_error_component import ApiV1AlertsCreateStatusErrorComponent
        from ..models.api_v1_alerts_create_suppressed_error_component import ApiV1AlertsCreateSuppressedErrorComponent
        from ..models.api_v1_alerts_create_target_availability_error_component import (
            ApiV1AlertsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_create_title_error_component import ApiV1AlertsCreateTitleErrorComponent
        from ..models.api_v1_alerts_create_tolerations_error_component import ApiV1AlertsCreateTolerationsErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateMessageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateLastSeenErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSuppressedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreatePodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateDashboardUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreatePanelUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSilenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateSilenceEndsAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateGeneratorUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_alerts_create_alert_router_error_component import (
            ApiV1AlertsCreateAlertRouterErrorComponent,
        )
        from ..models.api_v1_alerts_create_annotations_error_component import ApiV1AlertsCreateAnnotationsErrorComponent
        from ..models.api_v1_alerts_create_archived_at_error_component import ApiV1AlertsCreateArchivedAtErrorComponent
        from ..models.api_v1_alerts_create_archived_error_component import ApiV1AlertsCreateArchivedErrorComponent
        from ..models.api_v1_alerts_create_archived_reason_error_component import (
            ApiV1AlertsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alerts_create_block_error_component import ApiV1AlertsCreateBlockErrorComponent
        from ..models.api_v1_alerts_create_category_error_component import ApiV1AlertsCreateCategoryErrorComponent
        from ..models.api_v1_alerts_create_criticality_error_component import ApiV1AlertsCreateCriticalityErrorComponent
        from ..models.api_v1_alerts_create_dashboard_url_error_component import (
            ApiV1AlertsCreateDashboardUrlErrorComponent,
        )
        from ..models.api_v1_alerts_create_debug_mode_error_component import ApiV1AlertsCreateDebugModeErrorComponent
        from ..models.api_v1_alerts_create_display_name_error_component import (
            ApiV1AlertsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alerts_create_external_url_error_component import (
            ApiV1AlertsCreateExternalUrlErrorComponent,
        )
        from ..models.api_v1_alerts_create_fingerprint_error_component import ApiV1AlertsCreateFingerprintErrorComponent
        from ..models.api_v1_alerts_create_generator_url_error_component import (
            ApiV1AlertsCreateGeneratorUrlErrorComponent,
        )
        from ..models.api_v1_alerts_create_k8s_app_error_component import ApiV1AlertsCreateK8SAppErrorComponent
        from ..models.api_v1_alerts_create_k8s_cluster_error_component import ApiV1AlertsCreateK8SClusterErrorComponent
        from ..models.api_v1_alerts_create_kind_error_component import ApiV1AlertsCreateKindErrorComponent
        from ..models.api_v1_alerts_create_labels_error_component import ApiV1AlertsCreateLabelsErrorComponent
        from ..models.api_v1_alerts_create_last_seen_error_component import ApiV1AlertsCreateLastSeenErrorComponent
        from ..models.api_v1_alerts_create_message_error_component import ApiV1AlertsCreateMessageErrorComponent
        from ..models.api_v1_alerts_create_name_error_component import ApiV1AlertsCreateNameErrorComponent
        from ..models.api_v1_alerts_create_namespace_error_component import ApiV1AlertsCreateNamespaceErrorComponent
        from ..models.api_v1_alerts_create_non_field_errors_error_component import (
            ApiV1AlertsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alerts_create_panel_url_error_component import ApiV1AlertsCreatePanelUrlErrorComponent
        from ..models.api_v1_alerts_create_platform_service_error_component import (
            ApiV1AlertsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alerts_create_pod_error_component import ApiV1AlertsCreatePodErrorComponent
        from ..models.api_v1_alerts_create_provider_error_component import ApiV1AlertsCreateProviderErrorComponent
        from ..models.api_v1_alerts_create_provider_id_error_component import ApiV1AlertsCreateProviderIdErrorComponent
        from ..models.api_v1_alerts_create_provider_reference_error_component import (
            ApiV1AlertsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alerts_create_reconciliation_enabled_error_component import (
            ApiV1AlertsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alerts_create_silence_ends_at_error_component import (
            ApiV1AlertsCreateSilenceEndsAtErrorComponent,
        )
        from ..models.api_v1_alerts_create_silence_url_error_component import ApiV1AlertsCreateSilenceUrlErrorComponent
        from ..models.api_v1_alerts_create_sla_availability_error_component import (
            ApiV1AlertsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_create_sla_target_error_component import ApiV1AlertsCreateSlaTargetErrorComponent
        from ..models.api_v1_alerts_create_slo_availability_error_component import (
            ApiV1AlertsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_create_slo_target_error_component import ApiV1AlertsCreateSloTargetErrorComponent
        from ..models.api_v1_alerts_create_status_error_component import ApiV1AlertsCreateStatusErrorComponent
        from ..models.api_v1_alerts_create_suppressed_error_component import ApiV1AlertsCreateSuppressedErrorComponent
        from ..models.api_v1_alerts_create_target_availability_error_component import (
            ApiV1AlertsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_create_title_error_component import ApiV1AlertsCreateTitleErrorComponent
        from ..models.api_v1_alerts_create_tolerations_error_component import ApiV1AlertsCreateTolerationsErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsCreateAlertRouterErrorComponent
                | ApiV1AlertsCreateAnnotationsErrorComponent
                | ApiV1AlertsCreateArchivedAtErrorComponent
                | ApiV1AlertsCreateArchivedErrorComponent
                | ApiV1AlertsCreateArchivedReasonErrorComponent
                | ApiV1AlertsCreateBlockErrorComponent
                | ApiV1AlertsCreateCategoryErrorComponent
                | ApiV1AlertsCreateCriticalityErrorComponent
                | ApiV1AlertsCreateDashboardUrlErrorComponent
                | ApiV1AlertsCreateDebugModeErrorComponent
                | ApiV1AlertsCreateDisplayNameErrorComponent
                | ApiV1AlertsCreateExternalUrlErrorComponent
                | ApiV1AlertsCreateFingerprintErrorComponent
                | ApiV1AlertsCreateGeneratorUrlErrorComponent
                | ApiV1AlertsCreateK8SAppErrorComponent
                | ApiV1AlertsCreateK8SClusterErrorComponent
                | ApiV1AlertsCreateKindErrorComponent
                | ApiV1AlertsCreateLabelsErrorComponent
                | ApiV1AlertsCreateLastSeenErrorComponent
                | ApiV1AlertsCreateMessageErrorComponent
                | ApiV1AlertsCreateNameErrorComponent
                | ApiV1AlertsCreateNamespaceErrorComponent
                | ApiV1AlertsCreateNonFieldErrorsErrorComponent
                | ApiV1AlertsCreatePanelUrlErrorComponent
                | ApiV1AlertsCreatePlatformServiceErrorComponent
                | ApiV1AlertsCreatePodErrorComponent
                | ApiV1AlertsCreateProviderErrorComponent
                | ApiV1AlertsCreateProviderIdErrorComponent
                | ApiV1AlertsCreateProviderReferenceErrorComponent
                | ApiV1AlertsCreateReconciliationEnabledErrorComponent
                | ApiV1AlertsCreateSilenceEndsAtErrorComponent
                | ApiV1AlertsCreateSilenceUrlErrorComponent
                | ApiV1AlertsCreateSlaAvailabilityErrorComponent
                | ApiV1AlertsCreateSlaTargetErrorComponent
                | ApiV1AlertsCreateSloAvailabilityErrorComponent
                | ApiV1AlertsCreateSloTargetErrorComponent
                | ApiV1AlertsCreateStatusErrorComponent
                | ApiV1AlertsCreateSuppressedErrorComponent
                | ApiV1AlertsCreateTargetAvailabilityErrorComponent
                | ApiV1AlertsCreateTitleErrorComponent
                | ApiV1AlertsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_0 = (
                        ApiV1AlertsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_1 = ApiV1AlertsCreateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_2 = (
                        ApiV1AlertsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_3 = (
                        ApiV1AlertsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_4 = (
                        ApiV1AlertsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_5 = (
                        ApiV1AlertsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_6 = (
                        ApiV1AlertsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_7 = (
                        ApiV1AlertsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_8 = (
                        ApiV1AlertsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_9 = (
                        ApiV1AlertsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_10 = (
                        ApiV1AlertsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_11 = (
                        ApiV1AlertsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_12 = (
                        ApiV1AlertsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_13 = (
                        ApiV1AlertsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_14 = (
                        ApiV1AlertsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_15 = (
                        ApiV1AlertsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_16 = (
                        ApiV1AlertsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_17 = (
                        ApiV1AlertsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_18 = (
                        ApiV1AlertsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_19 = (
                        ApiV1AlertsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_20 = (
                        ApiV1AlertsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_21 = (
                        ApiV1AlertsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_22 = (
                        ApiV1AlertsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_23 = (
                        ApiV1AlertsCreateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_24 = (
                        ApiV1AlertsCreateFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_25 = (
                        ApiV1AlertsCreateExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_26 = (
                        ApiV1AlertsCreateMessageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_27 = (
                        ApiV1AlertsCreateLastSeenErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_28 = (
                        ApiV1AlertsCreateSuppressedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_29 = ApiV1AlertsCreatePodErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_30 = (
                        ApiV1AlertsCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_31 = (
                        ApiV1AlertsCreateCategoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_32 = (
                        ApiV1AlertsCreateDashboardUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_33 = (
                        ApiV1AlertsCreatePanelUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_34 = (
                        ApiV1AlertsCreateSilenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_35 = (
                        ApiV1AlertsCreateSilenceEndsAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_36 = (
                        ApiV1AlertsCreateGeneratorUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_37 = (
                        ApiV1AlertsCreateAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_38 = (
                        ApiV1AlertsCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_create_error_type_39 = (
                        ApiV1AlertsCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_create_error_type_40 = ApiV1AlertsCreateBlockErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_alerts_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_create_validation_error.additional_properties = d
        return api_v1_alerts_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
