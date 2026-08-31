from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_reconcile_create_alert_router_error_component import (
        ApiV1AlertsReconcileCreateAlertRouterErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_annotations_error_component import (
        ApiV1AlertsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_archived_at_error_component import (
        ApiV1AlertsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_archived_error_component import (
        ApiV1AlertsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_archived_reason_error_component import (
        ApiV1AlertsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_block_error_component import (
        ApiV1AlertsReconcileCreateBlockErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_category_error_component import (
        ApiV1AlertsReconcileCreateCategoryErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_criticality_error_component import (
        ApiV1AlertsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_dashboard_url_error_component import (
        ApiV1AlertsReconcileCreateDashboardUrlErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_debug_mode_error_component import (
        ApiV1AlertsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_display_name_error_component import (
        ApiV1AlertsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_external_url_error_component import (
        ApiV1AlertsReconcileCreateExternalUrlErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_fingerprint_error_component import (
        ApiV1AlertsReconcileCreateFingerprintErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_generator_url_error_component import (
        ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_k8s_app_error_component import (
        ApiV1AlertsReconcileCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_k8s_cluster_error_component import (
        ApiV1AlertsReconcileCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_kind_error_component import (
        ApiV1AlertsReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_labels_error_component import (
        ApiV1AlertsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_last_seen_error_component import (
        ApiV1AlertsReconcileCreateLastSeenErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_message_error_component import (
        ApiV1AlertsReconcileCreateMessageErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_name_error_component import (
        ApiV1AlertsReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_namespace_error_component import (
        ApiV1AlertsReconcileCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_non_field_errors_error_component import (
        ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_panel_url_error_component import (
        ApiV1AlertsReconcileCreatePanelUrlErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_platform_service_error_component import (
        ApiV1AlertsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_pod_error_component import ApiV1AlertsReconcileCreatePodErrorComponent
    from ..models.api_v1_alerts_reconcile_create_provider_error_component import (
        ApiV1AlertsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_provider_id_error_component import (
        ApiV1AlertsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_provider_reference_error_component import (
        ApiV1AlertsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_silence_ends_at_error_component import (
        ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_silence_url_error_component import (
        ApiV1AlertsReconcileCreateSilenceUrlErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_sla_availability_error_component import (
        ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_sla_target_error_component import (
        ApiV1AlertsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_slo_availability_error_component import (
        ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_slo_target_error_component import (
        ApiV1AlertsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_status_error_component import (
        ApiV1AlertsReconcileCreateStatusErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_suppressed_error_component import (
        ApiV1AlertsReconcileCreateSuppressedErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_target_availability_error_component import (
        ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_title_error_component import (
        ApiV1AlertsReconcileCreateTitleErrorComponent,
    )
    from ..models.api_v1_alerts_reconcile_create_tolerations_error_component import (
        ApiV1AlertsReconcileCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertsReconcileCreateValidationError")


@_attrs_define
class ApiV1AlertsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsReconcileCreateAlertRouterErrorComponent |
            ApiV1AlertsReconcileCreateAnnotationsErrorComponent | ApiV1AlertsReconcileCreateArchivedAtErrorComponent |
            ApiV1AlertsReconcileCreateArchivedErrorComponent | ApiV1AlertsReconcileCreateArchivedReasonErrorComponent |
            ApiV1AlertsReconcileCreateBlockErrorComponent | ApiV1AlertsReconcileCreateCategoryErrorComponent |
            ApiV1AlertsReconcileCreateCriticalityErrorComponent | ApiV1AlertsReconcileCreateDashboardUrlErrorComponent |
            ApiV1AlertsReconcileCreateDebugModeErrorComponent | ApiV1AlertsReconcileCreateDisplayNameErrorComponent |
            ApiV1AlertsReconcileCreateExternalUrlErrorComponent | ApiV1AlertsReconcileCreateFingerprintErrorComponent |
            ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent | ApiV1AlertsReconcileCreateK8SAppErrorComponent |
            ApiV1AlertsReconcileCreateK8SClusterErrorComponent | ApiV1AlertsReconcileCreateKindErrorComponent |
            ApiV1AlertsReconcileCreateLabelsErrorComponent | ApiV1AlertsReconcileCreateLastSeenErrorComponent |
            ApiV1AlertsReconcileCreateMessageErrorComponent | ApiV1AlertsReconcileCreateNameErrorComponent |
            ApiV1AlertsReconcileCreateNamespaceErrorComponent | ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1AlertsReconcileCreatePanelUrlErrorComponent | ApiV1AlertsReconcileCreatePlatformServiceErrorComponent |
            ApiV1AlertsReconcileCreatePodErrorComponent | ApiV1AlertsReconcileCreateProviderErrorComponent |
            ApiV1AlertsReconcileCreateProviderIdErrorComponent | ApiV1AlertsReconcileCreateProviderReferenceErrorComponent |
            ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent | ApiV1AlertsReconcileCreateSilenceUrlErrorComponent |
            ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent | ApiV1AlertsReconcileCreateSlaTargetErrorComponent |
            ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent | ApiV1AlertsReconcileCreateSloTargetErrorComponent |
            ApiV1AlertsReconcileCreateStatusErrorComponent | ApiV1AlertsReconcileCreateSuppressedErrorComponent |
            ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent | ApiV1AlertsReconcileCreateTitleErrorComponent |
            ApiV1AlertsReconcileCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsReconcileCreateAlertRouterErrorComponent
        | ApiV1AlertsReconcileCreateAnnotationsErrorComponent
        | ApiV1AlertsReconcileCreateArchivedAtErrorComponent
        | ApiV1AlertsReconcileCreateArchivedErrorComponent
        | ApiV1AlertsReconcileCreateArchivedReasonErrorComponent
        | ApiV1AlertsReconcileCreateBlockErrorComponent
        | ApiV1AlertsReconcileCreateCategoryErrorComponent
        | ApiV1AlertsReconcileCreateCriticalityErrorComponent
        | ApiV1AlertsReconcileCreateDashboardUrlErrorComponent
        | ApiV1AlertsReconcileCreateDebugModeErrorComponent
        | ApiV1AlertsReconcileCreateDisplayNameErrorComponent
        | ApiV1AlertsReconcileCreateExternalUrlErrorComponent
        | ApiV1AlertsReconcileCreateFingerprintErrorComponent
        | ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent
        | ApiV1AlertsReconcileCreateK8SAppErrorComponent
        | ApiV1AlertsReconcileCreateK8SClusterErrorComponent
        | ApiV1AlertsReconcileCreateKindErrorComponent
        | ApiV1AlertsReconcileCreateLabelsErrorComponent
        | ApiV1AlertsReconcileCreateLastSeenErrorComponent
        | ApiV1AlertsReconcileCreateMessageErrorComponent
        | ApiV1AlertsReconcileCreateNameErrorComponent
        | ApiV1AlertsReconcileCreateNamespaceErrorComponent
        | ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1AlertsReconcileCreatePanelUrlErrorComponent
        | ApiV1AlertsReconcileCreatePlatformServiceErrorComponent
        | ApiV1AlertsReconcileCreatePodErrorComponent
        | ApiV1AlertsReconcileCreateProviderErrorComponent
        | ApiV1AlertsReconcileCreateProviderIdErrorComponent
        | ApiV1AlertsReconcileCreateProviderReferenceErrorComponent
        | ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent
        | ApiV1AlertsReconcileCreateSilenceUrlErrorComponent
        | ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1AlertsReconcileCreateSlaTargetErrorComponent
        | ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1AlertsReconcileCreateSloTargetErrorComponent
        | ApiV1AlertsReconcileCreateStatusErrorComponent
        | ApiV1AlertsReconcileCreateSuppressedErrorComponent
        | ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1AlertsReconcileCreateTitleErrorComponent
        | ApiV1AlertsReconcileCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_reconcile_create_alert_router_error_component import (
            ApiV1AlertsReconcileCreateAlertRouterErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_annotations_error_component import (
            ApiV1AlertsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_archived_at_error_component import (
            ApiV1AlertsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_archived_error_component import (
            ApiV1AlertsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_archived_reason_error_component import (
            ApiV1AlertsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_category_error_component import (
            ApiV1AlertsReconcileCreateCategoryErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_criticality_error_component import (
            ApiV1AlertsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_dashboard_url_error_component import (
            ApiV1AlertsReconcileCreateDashboardUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_debug_mode_error_component import (
            ApiV1AlertsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_display_name_error_component import (
            ApiV1AlertsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_external_url_error_component import (
            ApiV1AlertsReconcileCreateExternalUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_fingerprint_error_component import (
            ApiV1AlertsReconcileCreateFingerprintErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_generator_url_error_component import (
            ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_k8s_app_error_component import (
            ApiV1AlertsReconcileCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_k8s_cluster_error_component import (
            ApiV1AlertsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_kind_error_component import (
            ApiV1AlertsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_labels_error_component import (
            ApiV1AlertsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_last_seen_error_component import (
            ApiV1AlertsReconcileCreateLastSeenErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_message_error_component import (
            ApiV1AlertsReconcileCreateMessageErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_name_error_component import (
            ApiV1AlertsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_namespace_error_component import (
            ApiV1AlertsReconcileCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_non_field_errors_error_component import (
            ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_panel_url_error_component import (
            ApiV1AlertsReconcileCreatePanelUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_platform_service_error_component import (
            ApiV1AlertsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_pod_error_component import (
            ApiV1AlertsReconcileCreatePodErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_provider_error_component import (
            ApiV1AlertsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_provider_id_error_component import (
            ApiV1AlertsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_provider_reference_error_component import (
            ApiV1AlertsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_silence_ends_at_error_component import (
            ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_silence_url_error_component import (
            ApiV1AlertsReconcileCreateSilenceUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_sla_availability_error_component import (
            ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_sla_target_error_component import (
            ApiV1AlertsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_slo_availability_error_component import (
            ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_slo_target_error_component import (
            ApiV1AlertsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_status_error_component import (
            ApiV1AlertsReconcileCreateStatusErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_suppressed_error_component import (
            ApiV1AlertsReconcileCreateSuppressedErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_target_availability_error_component import (
            ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_title_error_component import (
            ApiV1AlertsReconcileCreateTitleErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_tolerations_error_component import (
            ApiV1AlertsReconcileCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateMessageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateLastSeenErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSuppressedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreatePodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateDashboardUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreatePanelUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSilenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsReconcileCreateK8SAppErrorComponent):
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
        from ..models.api_v1_alerts_reconcile_create_alert_router_error_component import (
            ApiV1AlertsReconcileCreateAlertRouterErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_annotations_error_component import (
            ApiV1AlertsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_archived_at_error_component import (
            ApiV1AlertsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_archived_error_component import (
            ApiV1AlertsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_archived_reason_error_component import (
            ApiV1AlertsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_block_error_component import (
            ApiV1AlertsReconcileCreateBlockErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_category_error_component import (
            ApiV1AlertsReconcileCreateCategoryErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_criticality_error_component import (
            ApiV1AlertsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_dashboard_url_error_component import (
            ApiV1AlertsReconcileCreateDashboardUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_debug_mode_error_component import (
            ApiV1AlertsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_display_name_error_component import (
            ApiV1AlertsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_external_url_error_component import (
            ApiV1AlertsReconcileCreateExternalUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_fingerprint_error_component import (
            ApiV1AlertsReconcileCreateFingerprintErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_generator_url_error_component import (
            ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_k8s_app_error_component import (
            ApiV1AlertsReconcileCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_k8s_cluster_error_component import (
            ApiV1AlertsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_kind_error_component import (
            ApiV1AlertsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_labels_error_component import (
            ApiV1AlertsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_last_seen_error_component import (
            ApiV1AlertsReconcileCreateLastSeenErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_message_error_component import (
            ApiV1AlertsReconcileCreateMessageErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_name_error_component import (
            ApiV1AlertsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_namespace_error_component import (
            ApiV1AlertsReconcileCreateNamespaceErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_non_field_errors_error_component import (
            ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_panel_url_error_component import (
            ApiV1AlertsReconcileCreatePanelUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_platform_service_error_component import (
            ApiV1AlertsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_pod_error_component import (
            ApiV1AlertsReconcileCreatePodErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_provider_error_component import (
            ApiV1AlertsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_provider_id_error_component import (
            ApiV1AlertsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_provider_reference_error_component import (
            ApiV1AlertsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_silence_ends_at_error_component import (
            ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_silence_url_error_component import (
            ApiV1AlertsReconcileCreateSilenceUrlErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_sla_availability_error_component import (
            ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_sla_target_error_component import (
            ApiV1AlertsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_slo_availability_error_component import (
            ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_slo_target_error_component import (
            ApiV1AlertsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_status_error_component import (
            ApiV1AlertsReconcileCreateStatusErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_suppressed_error_component import (
            ApiV1AlertsReconcileCreateSuppressedErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_target_availability_error_component import (
            ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_title_error_component import (
            ApiV1AlertsReconcileCreateTitleErrorComponent,
        )
        from ..models.api_v1_alerts_reconcile_create_tolerations_error_component import (
            ApiV1AlertsReconcileCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsReconcileCreateAlertRouterErrorComponent
                | ApiV1AlertsReconcileCreateAnnotationsErrorComponent
                | ApiV1AlertsReconcileCreateArchivedAtErrorComponent
                | ApiV1AlertsReconcileCreateArchivedErrorComponent
                | ApiV1AlertsReconcileCreateArchivedReasonErrorComponent
                | ApiV1AlertsReconcileCreateBlockErrorComponent
                | ApiV1AlertsReconcileCreateCategoryErrorComponent
                | ApiV1AlertsReconcileCreateCriticalityErrorComponent
                | ApiV1AlertsReconcileCreateDashboardUrlErrorComponent
                | ApiV1AlertsReconcileCreateDebugModeErrorComponent
                | ApiV1AlertsReconcileCreateDisplayNameErrorComponent
                | ApiV1AlertsReconcileCreateExternalUrlErrorComponent
                | ApiV1AlertsReconcileCreateFingerprintErrorComponent
                | ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent
                | ApiV1AlertsReconcileCreateK8SAppErrorComponent
                | ApiV1AlertsReconcileCreateK8SClusterErrorComponent
                | ApiV1AlertsReconcileCreateKindErrorComponent
                | ApiV1AlertsReconcileCreateLabelsErrorComponent
                | ApiV1AlertsReconcileCreateLastSeenErrorComponent
                | ApiV1AlertsReconcileCreateMessageErrorComponent
                | ApiV1AlertsReconcileCreateNameErrorComponent
                | ApiV1AlertsReconcileCreateNamespaceErrorComponent
                | ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1AlertsReconcileCreatePanelUrlErrorComponent
                | ApiV1AlertsReconcileCreatePlatformServiceErrorComponent
                | ApiV1AlertsReconcileCreatePodErrorComponent
                | ApiV1AlertsReconcileCreateProviderErrorComponent
                | ApiV1AlertsReconcileCreateProviderIdErrorComponent
                | ApiV1AlertsReconcileCreateProviderReferenceErrorComponent
                | ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent
                | ApiV1AlertsReconcileCreateSilenceUrlErrorComponent
                | ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1AlertsReconcileCreateSlaTargetErrorComponent
                | ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1AlertsReconcileCreateSloTargetErrorComponent
                | ApiV1AlertsReconcileCreateStatusErrorComponent
                | ApiV1AlertsReconcileCreateSuppressedErrorComponent
                | ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1AlertsReconcileCreateTitleErrorComponent
                | ApiV1AlertsReconcileCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_0 = (
                        ApiV1AlertsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_1 = (
                        ApiV1AlertsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_2 = (
                        ApiV1AlertsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_3 = (
                        ApiV1AlertsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_4 = (
                        ApiV1AlertsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_5 = (
                        ApiV1AlertsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_6 = (
                        ApiV1AlertsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_7 = (
                        ApiV1AlertsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_8 = (
                        ApiV1AlertsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_9 = (
                        ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_10 = (
                        ApiV1AlertsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_11 = (
                        ApiV1AlertsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_12 = (
                        ApiV1AlertsReconcileCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_13 = (
                        ApiV1AlertsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_14 = (
                        ApiV1AlertsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_15 = (
                        ApiV1AlertsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_16 = (
                        ApiV1AlertsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_17 = (
                        ApiV1AlertsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_18 = (
                        ApiV1AlertsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_19 = (
                        ApiV1AlertsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_20 = (
                        ApiV1AlertsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_21 = (
                        ApiV1AlertsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_22 = (
                        ApiV1AlertsReconcileCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_23 = (
                        ApiV1AlertsReconcileCreateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_24 = (
                        ApiV1AlertsReconcileCreateFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_25 = (
                        ApiV1AlertsReconcileCreateExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_26 = (
                        ApiV1AlertsReconcileCreateMessageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_27 = (
                        ApiV1AlertsReconcileCreateLastSeenErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_28 = (
                        ApiV1AlertsReconcileCreateSuppressedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_29 = (
                        ApiV1AlertsReconcileCreatePodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_30 = (
                        ApiV1AlertsReconcileCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_31 = (
                        ApiV1AlertsReconcileCreateCategoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_32 = (
                        ApiV1AlertsReconcileCreateDashboardUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_33 = (
                        ApiV1AlertsReconcileCreatePanelUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_34 = (
                        ApiV1AlertsReconcileCreateSilenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_35 = (
                        ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_36 = (
                        ApiV1AlertsReconcileCreateGeneratorUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_37 = (
                        ApiV1AlertsReconcileCreateAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_38 = (
                        ApiV1AlertsReconcileCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_reconcile_create_error_type_39 = (
                        ApiV1AlertsReconcileCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_reconcile_create_error_type_40 = (
                    ApiV1AlertsReconcileCreateBlockErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alerts_reconcile_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_reconcile_create_validation_error.additional_properties = d
        return api_v1_alerts_reconcile_create_validation_error

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
