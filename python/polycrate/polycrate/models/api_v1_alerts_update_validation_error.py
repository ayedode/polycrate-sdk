from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_update_alert_router_error_component import ApiV1AlertsUpdateAlertRouterErrorComponent
    from ..models.api_v1_alerts_update_annotations_error_component import ApiV1AlertsUpdateAnnotationsErrorComponent
    from ..models.api_v1_alerts_update_archived_at_error_component import ApiV1AlertsUpdateArchivedAtErrorComponent
    from ..models.api_v1_alerts_update_archived_error_component import ApiV1AlertsUpdateArchivedErrorComponent
    from ..models.api_v1_alerts_update_archived_reason_error_component import (
        ApiV1AlertsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alerts_update_block_error_component import ApiV1AlertsUpdateBlockErrorComponent
    from ..models.api_v1_alerts_update_category_error_component import ApiV1AlertsUpdateCategoryErrorComponent
    from ..models.api_v1_alerts_update_criticality_error_component import ApiV1AlertsUpdateCriticalityErrorComponent
    from ..models.api_v1_alerts_update_dashboard_url_error_component import ApiV1AlertsUpdateDashboardUrlErrorComponent
    from ..models.api_v1_alerts_update_debug_mode_error_component import ApiV1AlertsUpdateDebugModeErrorComponent
    from ..models.api_v1_alerts_update_display_name_error_component import ApiV1AlertsUpdateDisplayNameErrorComponent
    from ..models.api_v1_alerts_update_external_url_error_component import ApiV1AlertsUpdateExternalUrlErrorComponent
    from ..models.api_v1_alerts_update_fingerprint_error_component import ApiV1AlertsUpdateFingerprintErrorComponent
    from ..models.api_v1_alerts_update_generator_url_error_component import ApiV1AlertsUpdateGeneratorUrlErrorComponent
    from ..models.api_v1_alerts_update_k8s_app_error_component import ApiV1AlertsUpdateK8SAppErrorComponent
    from ..models.api_v1_alerts_update_k8s_cluster_error_component import ApiV1AlertsUpdateK8SClusterErrorComponent
    from ..models.api_v1_alerts_update_kind_error_component import ApiV1AlertsUpdateKindErrorComponent
    from ..models.api_v1_alerts_update_labels_error_component import ApiV1AlertsUpdateLabelsErrorComponent
    from ..models.api_v1_alerts_update_last_seen_error_component import ApiV1AlertsUpdateLastSeenErrorComponent
    from ..models.api_v1_alerts_update_message_error_component import ApiV1AlertsUpdateMessageErrorComponent
    from ..models.api_v1_alerts_update_name_error_component import ApiV1AlertsUpdateNameErrorComponent
    from ..models.api_v1_alerts_update_namespace_error_component import ApiV1AlertsUpdateNamespaceErrorComponent
    from ..models.api_v1_alerts_update_non_field_errors_error_component import (
        ApiV1AlertsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alerts_update_panel_url_error_component import ApiV1AlertsUpdatePanelUrlErrorComponent
    from ..models.api_v1_alerts_update_platform_service_error_component import (
        ApiV1AlertsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alerts_update_pod_error_component import ApiV1AlertsUpdatePodErrorComponent
    from ..models.api_v1_alerts_update_provider_error_component import ApiV1AlertsUpdateProviderErrorComponent
    from ..models.api_v1_alerts_update_provider_id_error_component import ApiV1AlertsUpdateProviderIdErrorComponent
    from ..models.api_v1_alerts_update_provider_reference_error_component import (
        ApiV1AlertsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alerts_update_reconciliation_enabled_error_component import (
        ApiV1AlertsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alerts_update_silence_ends_at_error_component import (
        ApiV1AlertsUpdateSilenceEndsAtErrorComponent,
    )
    from ..models.api_v1_alerts_update_silence_url_error_component import ApiV1AlertsUpdateSilenceUrlErrorComponent
    from ..models.api_v1_alerts_update_sla_availability_error_component import (
        ApiV1AlertsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_update_sla_target_error_component import ApiV1AlertsUpdateSlaTargetErrorComponent
    from ..models.api_v1_alerts_update_slo_availability_error_component import (
        ApiV1AlertsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_update_slo_target_error_component import ApiV1AlertsUpdateSloTargetErrorComponent
    from ..models.api_v1_alerts_update_status_error_component import ApiV1AlertsUpdateStatusErrorComponent
    from ..models.api_v1_alerts_update_suppressed_error_component import ApiV1AlertsUpdateSuppressedErrorComponent
    from ..models.api_v1_alerts_update_target_availability_error_component import (
        ApiV1AlertsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_update_title_error_component import ApiV1AlertsUpdateTitleErrorComponent
    from ..models.api_v1_alerts_update_tolerations_error_component import ApiV1AlertsUpdateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1AlertsUpdateValidationError")


@_attrs_define
class ApiV1AlertsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsUpdateAlertRouterErrorComponent | ApiV1AlertsUpdateAnnotationsErrorComponent |
            ApiV1AlertsUpdateArchivedAtErrorComponent | ApiV1AlertsUpdateArchivedErrorComponent |
            ApiV1AlertsUpdateArchivedReasonErrorComponent | ApiV1AlertsUpdateBlockErrorComponent |
            ApiV1AlertsUpdateCategoryErrorComponent | ApiV1AlertsUpdateCriticalityErrorComponent |
            ApiV1AlertsUpdateDashboardUrlErrorComponent | ApiV1AlertsUpdateDebugModeErrorComponent |
            ApiV1AlertsUpdateDisplayNameErrorComponent | ApiV1AlertsUpdateExternalUrlErrorComponent |
            ApiV1AlertsUpdateFingerprintErrorComponent | ApiV1AlertsUpdateGeneratorUrlErrorComponent |
            ApiV1AlertsUpdateK8SAppErrorComponent | ApiV1AlertsUpdateK8SClusterErrorComponent |
            ApiV1AlertsUpdateKindErrorComponent | ApiV1AlertsUpdateLabelsErrorComponent |
            ApiV1AlertsUpdateLastSeenErrorComponent | ApiV1AlertsUpdateMessageErrorComponent |
            ApiV1AlertsUpdateNameErrorComponent | ApiV1AlertsUpdateNamespaceErrorComponent |
            ApiV1AlertsUpdateNonFieldErrorsErrorComponent | ApiV1AlertsUpdatePanelUrlErrorComponent |
            ApiV1AlertsUpdatePlatformServiceErrorComponent | ApiV1AlertsUpdatePodErrorComponent |
            ApiV1AlertsUpdateProviderErrorComponent | ApiV1AlertsUpdateProviderIdErrorComponent |
            ApiV1AlertsUpdateProviderReferenceErrorComponent | ApiV1AlertsUpdateReconciliationEnabledErrorComponent |
            ApiV1AlertsUpdateSilenceEndsAtErrorComponent | ApiV1AlertsUpdateSilenceUrlErrorComponent |
            ApiV1AlertsUpdateSlaAvailabilityErrorComponent | ApiV1AlertsUpdateSlaTargetErrorComponent |
            ApiV1AlertsUpdateSloAvailabilityErrorComponent | ApiV1AlertsUpdateSloTargetErrorComponent |
            ApiV1AlertsUpdateStatusErrorComponent | ApiV1AlertsUpdateSuppressedErrorComponent |
            ApiV1AlertsUpdateTargetAvailabilityErrorComponent | ApiV1AlertsUpdateTitleErrorComponent |
            ApiV1AlertsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsUpdateAlertRouterErrorComponent
        | ApiV1AlertsUpdateAnnotationsErrorComponent
        | ApiV1AlertsUpdateArchivedAtErrorComponent
        | ApiV1AlertsUpdateArchivedErrorComponent
        | ApiV1AlertsUpdateArchivedReasonErrorComponent
        | ApiV1AlertsUpdateBlockErrorComponent
        | ApiV1AlertsUpdateCategoryErrorComponent
        | ApiV1AlertsUpdateCriticalityErrorComponent
        | ApiV1AlertsUpdateDashboardUrlErrorComponent
        | ApiV1AlertsUpdateDebugModeErrorComponent
        | ApiV1AlertsUpdateDisplayNameErrorComponent
        | ApiV1AlertsUpdateExternalUrlErrorComponent
        | ApiV1AlertsUpdateFingerprintErrorComponent
        | ApiV1AlertsUpdateGeneratorUrlErrorComponent
        | ApiV1AlertsUpdateK8SAppErrorComponent
        | ApiV1AlertsUpdateK8SClusterErrorComponent
        | ApiV1AlertsUpdateKindErrorComponent
        | ApiV1AlertsUpdateLabelsErrorComponent
        | ApiV1AlertsUpdateLastSeenErrorComponent
        | ApiV1AlertsUpdateMessageErrorComponent
        | ApiV1AlertsUpdateNameErrorComponent
        | ApiV1AlertsUpdateNamespaceErrorComponent
        | ApiV1AlertsUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertsUpdatePanelUrlErrorComponent
        | ApiV1AlertsUpdatePlatformServiceErrorComponent
        | ApiV1AlertsUpdatePodErrorComponent
        | ApiV1AlertsUpdateProviderErrorComponent
        | ApiV1AlertsUpdateProviderIdErrorComponent
        | ApiV1AlertsUpdateProviderReferenceErrorComponent
        | ApiV1AlertsUpdateReconciliationEnabledErrorComponent
        | ApiV1AlertsUpdateSilenceEndsAtErrorComponent
        | ApiV1AlertsUpdateSilenceUrlErrorComponent
        | ApiV1AlertsUpdateSlaAvailabilityErrorComponent
        | ApiV1AlertsUpdateSlaTargetErrorComponent
        | ApiV1AlertsUpdateSloAvailabilityErrorComponent
        | ApiV1AlertsUpdateSloTargetErrorComponent
        | ApiV1AlertsUpdateStatusErrorComponent
        | ApiV1AlertsUpdateSuppressedErrorComponent
        | ApiV1AlertsUpdateTargetAvailabilityErrorComponent
        | ApiV1AlertsUpdateTitleErrorComponent
        | ApiV1AlertsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_update_alert_router_error_component import (
            ApiV1AlertsUpdateAlertRouterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_annotations_error_component import (
            ApiV1AlertsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_archived_at_error_component import (
            ApiV1AlertsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_archived_error_component import (
            ApiV1AlertsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_archived_reason_error_component import (
            ApiV1AlertsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_category_error_component import (
            ApiV1AlertsUpdateCategoryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_criticality_error_component import (
            ApiV1AlertsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_dashboard_url_error_component import (
            ApiV1AlertsUpdateDashboardUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_debug_mode_error_component import (
            ApiV1AlertsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_display_name_error_component import (
            ApiV1AlertsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_external_url_error_component import (
            ApiV1AlertsUpdateExternalUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_fingerprint_error_component import (
            ApiV1AlertsUpdateFingerprintErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_generator_url_error_component import (
            ApiV1AlertsUpdateGeneratorUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_k8s_app_error_component import (
            ApiV1AlertsUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_k8s_cluster_error_component import (
            ApiV1AlertsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_kind_error_component import (
            ApiV1AlertsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_labels_error_component import (
            ApiV1AlertsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_last_seen_error_component import (
            ApiV1AlertsUpdateLastSeenErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_message_error_component import (
            ApiV1AlertsUpdateMessageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_name_error_component import (
            ApiV1AlertsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_namespace_error_component import (
            ApiV1AlertsUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_non_field_errors_error_component import (
            ApiV1AlertsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_panel_url_error_component import (
            ApiV1AlertsUpdatePanelUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_platform_service_error_component import (
            ApiV1AlertsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_pod_error_component import (
            ApiV1AlertsUpdatePodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_provider_error_component import (
            ApiV1AlertsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_provider_id_error_component import (
            ApiV1AlertsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_provider_reference_error_component import (
            ApiV1AlertsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_reconciliation_enabled_error_component import (
            ApiV1AlertsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_silence_ends_at_error_component import (
            ApiV1AlertsUpdateSilenceEndsAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_silence_url_error_component import (
            ApiV1AlertsUpdateSilenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_sla_availability_error_component import (
            ApiV1AlertsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_sla_target_error_component import (
            ApiV1AlertsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_slo_availability_error_component import (
            ApiV1AlertsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_slo_target_error_component import (
            ApiV1AlertsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_status_error_component import (
            ApiV1AlertsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_suppressed_error_component import (
            ApiV1AlertsUpdateSuppressedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_target_availability_error_component import (
            ApiV1AlertsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_title_error_component import (
            ApiV1AlertsUpdateTitleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_tolerations_error_component import (
            ApiV1AlertsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateMessageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateLastSeenErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSuppressedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdatePodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateDashboardUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdatePanelUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSilenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateSilenceEndsAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateGeneratorUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsUpdateK8SAppErrorComponent):
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
        from ..models.api_v1_alerts_update_alert_router_error_component import (
            ApiV1AlertsUpdateAlertRouterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_annotations_error_component import (
            ApiV1AlertsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_archived_at_error_component import (
            ApiV1AlertsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_archived_error_component import (
            ApiV1AlertsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_archived_reason_error_component import (
            ApiV1AlertsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_block_error_component import (
            ApiV1AlertsUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_category_error_component import (
            ApiV1AlertsUpdateCategoryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_criticality_error_component import (
            ApiV1AlertsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_dashboard_url_error_component import (
            ApiV1AlertsUpdateDashboardUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_debug_mode_error_component import (
            ApiV1AlertsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_display_name_error_component import (
            ApiV1AlertsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_external_url_error_component import (
            ApiV1AlertsUpdateExternalUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_fingerprint_error_component import (
            ApiV1AlertsUpdateFingerprintErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_generator_url_error_component import (
            ApiV1AlertsUpdateGeneratorUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_k8s_app_error_component import (
            ApiV1AlertsUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_k8s_cluster_error_component import (
            ApiV1AlertsUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_kind_error_component import (
            ApiV1AlertsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_labels_error_component import (
            ApiV1AlertsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_last_seen_error_component import (
            ApiV1AlertsUpdateLastSeenErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_message_error_component import (
            ApiV1AlertsUpdateMessageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_name_error_component import (
            ApiV1AlertsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_namespace_error_component import (
            ApiV1AlertsUpdateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_non_field_errors_error_component import (
            ApiV1AlertsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_panel_url_error_component import (
            ApiV1AlertsUpdatePanelUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_platform_service_error_component import (
            ApiV1AlertsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_pod_error_component import (
            ApiV1AlertsUpdatePodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_provider_error_component import (
            ApiV1AlertsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_provider_id_error_component import (
            ApiV1AlertsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_provider_reference_error_component import (
            ApiV1AlertsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_reconciliation_enabled_error_component import (
            ApiV1AlertsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_silence_ends_at_error_component import (
            ApiV1AlertsUpdateSilenceEndsAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_silence_url_error_component import (
            ApiV1AlertsUpdateSilenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_sla_availability_error_component import (
            ApiV1AlertsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_sla_target_error_component import (
            ApiV1AlertsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_slo_availability_error_component import (
            ApiV1AlertsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_slo_target_error_component import (
            ApiV1AlertsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_status_error_component import (
            ApiV1AlertsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_suppressed_error_component import (
            ApiV1AlertsUpdateSuppressedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_target_availability_error_component import (
            ApiV1AlertsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_title_error_component import (
            ApiV1AlertsUpdateTitleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_update_tolerations_error_component import (
            ApiV1AlertsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsUpdateAlertRouterErrorComponent
                | ApiV1AlertsUpdateAnnotationsErrorComponent
                | ApiV1AlertsUpdateArchivedAtErrorComponent
                | ApiV1AlertsUpdateArchivedErrorComponent
                | ApiV1AlertsUpdateArchivedReasonErrorComponent
                | ApiV1AlertsUpdateBlockErrorComponent
                | ApiV1AlertsUpdateCategoryErrorComponent
                | ApiV1AlertsUpdateCriticalityErrorComponent
                | ApiV1AlertsUpdateDashboardUrlErrorComponent
                | ApiV1AlertsUpdateDebugModeErrorComponent
                | ApiV1AlertsUpdateDisplayNameErrorComponent
                | ApiV1AlertsUpdateExternalUrlErrorComponent
                | ApiV1AlertsUpdateFingerprintErrorComponent
                | ApiV1AlertsUpdateGeneratorUrlErrorComponent
                | ApiV1AlertsUpdateK8SAppErrorComponent
                | ApiV1AlertsUpdateK8SClusterErrorComponent
                | ApiV1AlertsUpdateKindErrorComponent
                | ApiV1AlertsUpdateLabelsErrorComponent
                | ApiV1AlertsUpdateLastSeenErrorComponent
                | ApiV1AlertsUpdateMessageErrorComponent
                | ApiV1AlertsUpdateNameErrorComponent
                | ApiV1AlertsUpdateNamespaceErrorComponent
                | ApiV1AlertsUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertsUpdatePanelUrlErrorComponent
                | ApiV1AlertsUpdatePlatformServiceErrorComponent
                | ApiV1AlertsUpdatePodErrorComponent
                | ApiV1AlertsUpdateProviderErrorComponent
                | ApiV1AlertsUpdateProviderIdErrorComponent
                | ApiV1AlertsUpdateProviderReferenceErrorComponent
                | ApiV1AlertsUpdateReconciliationEnabledErrorComponent
                | ApiV1AlertsUpdateSilenceEndsAtErrorComponent
                | ApiV1AlertsUpdateSilenceUrlErrorComponent
                | ApiV1AlertsUpdateSlaAvailabilityErrorComponent
                | ApiV1AlertsUpdateSlaTargetErrorComponent
                | ApiV1AlertsUpdateSloAvailabilityErrorComponent
                | ApiV1AlertsUpdateSloTargetErrorComponent
                | ApiV1AlertsUpdateStatusErrorComponent
                | ApiV1AlertsUpdateSuppressedErrorComponent
                | ApiV1AlertsUpdateTargetAvailabilityErrorComponent
                | ApiV1AlertsUpdateTitleErrorComponent
                | ApiV1AlertsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_0 = (
                        ApiV1AlertsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_1 = ApiV1AlertsUpdateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_2 = (
                        ApiV1AlertsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_3 = (
                        ApiV1AlertsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_4 = (
                        ApiV1AlertsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_5 = (
                        ApiV1AlertsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_6 = (
                        ApiV1AlertsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_7 = (
                        ApiV1AlertsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_8 = (
                        ApiV1AlertsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_9 = (
                        ApiV1AlertsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_10 = (
                        ApiV1AlertsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_11 = (
                        ApiV1AlertsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_12 = (
                        ApiV1AlertsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_13 = (
                        ApiV1AlertsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_14 = (
                        ApiV1AlertsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_15 = (
                        ApiV1AlertsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_16 = (
                        ApiV1AlertsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_17 = (
                        ApiV1AlertsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_18 = (
                        ApiV1AlertsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_19 = (
                        ApiV1AlertsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_20 = (
                        ApiV1AlertsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_21 = (
                        ApiV1AlertsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_22 = (
                        ApiV1AlertsUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_23 = (
                        ApiV1AlertsUpdateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_24 = (
                        ApiV1AlertsUpdateFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_25 = (
                        ApiV1AlertsUpdateExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_26 = (
                        ApiV1AlertsUpdateMessageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_27 = (
                        ApiV1AlertsUpdateLastSeenErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_28 = (
                        ApiV1AlertsUpdateSuppressedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_29 = ApiV1AlertsUpdatePodErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_30 = (
                        ApiV1AlertsUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_31 = (
                        ApiV1AlertsUpdateCategoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_32 = (
                        ApiV1AlertsUpdateDashboardUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_33 = (
                        ApiV1AlertsUpdatePanelUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_34 = (
                        ApiV1AlertsUpdateSilenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_35 = (
                        ApiV1AlertsUpdateSilenceEndsAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_36 = (
                        ApiV1AlertsUpdateGeneratorUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_37 = (
                        ApiV1AlertsUpdateAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_38 = (
                        ApiV1AlertsUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_update_error_type_39 = (
                        ApiV1AlertsUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_update_error_type_40 = ApiV1AlertsUpdateBlockErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_alerts_update_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_update_validation_error.additional_properties = d
        return api_v1_alerts_update_validation_error

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
