from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_discover_create_alert_router_error_component import (
        ApiV1AlertsDiscoverCreateAlertRouterErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_annotations_error_component import (
        ApiV1AlertsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_archived_at_error_component import (
        ApiV1AlertsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_archived_error_component import (
        ApiV1AlertsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_archived_reason_error_component import (
        ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_block_error_component import (
        ApiV1AlertsDiscoverCreateBlockErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_category_error_component import (
        ApiV1AlertsDiscoverCreateCategoryErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_criticality_error_component import (
        ApiV1AlertsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_dashboard_url_error_component import (
        ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_debug_mode_error_component import (
        ApiV1AlertsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_display_name_error_component import (
        ApiV1AlertsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_external_url_error_component import (
        ApiV1AlertsDiscoverCreateExternalUrlErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_fingerprint_error_component import (
        ApiV1AlertsDiscoverCreateFingerprintErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_generator_url_error_component import (
        ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_k8s_app_error_component import (
        ApiV1AlertsDiscoverCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_k8s_cluster_error_component import (
        ApiV1AlertsDiscoverCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_kind_error_component import ApiV1AlertsDiscoverCreateKindErrorComponent
    from ..models.api_v1_alerts_discover_create_labels_error_component import (
        ApiV1AlertsDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_last_seen_error_component import (
        ApiV1AlertsDiscoverCreateLastSeenErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_message_error_component import (
        ApiV1AlertsDiscoverCreateMessageErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_name_error_component import ApiV1AlertsDiscoverCreateNameErrorComponent
    from ..models.api_v1_alerts_discover_create_namespace_error_component import (
        ApiV1AlertsDiscoverCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_non_field_errors_error_component import (
        ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_panel_url_error_component import (
        ApiV1AlertsDiscoverCreatePanelUrlErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_platform_service_error_component import (
        ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_pod_error_component import ApiV1AlertsDiscoverCreatePodErrorComponent
    from ..models.api_v1_alerts_discover_create_provider_error_component import (
        ApiV1AlertsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_provider_id_error_component import (
        ApiV1AlertsDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_provider_reference_error_component import (
        ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_reconciliation_enabled_error_component import (
        ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_silence_ends_at_error_component import (
        ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_silence_url_error_component import (
        ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_sla_availability_error_component import (
        ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_sla_target_error_component import (
        ApiV1AlertsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_slo_availability_error_component import (
        ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_slo_target_error_component import (
        ApiV1AlertsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_status_error_component import (
        ApiV1AlertsDiscoverCreateStatusErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_suppressed_error_component import (
        ApiV1AlertsDiscoverCreateSuppressedErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_target_availability_error_component import (
        ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_title_error_component import (
        ApiV1AlertsDiscoverCreateTitleErrorComponent,
    )
    from ..models.api_v1_alerts_discover_create_tolerations_error_component import (
        ApiV1AlertsDiscoverCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertsDiscoverCreateValidationError")


@_attrs_define
class ApiV1AlertsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsDiscoverCreateAlertRouterErrorComponent |
            ApiV1AlertsDiscoverCreateAnnotationsErrorComponent | ApiV1AlertsDiscoverCreateArchivedAtErrorComponent |
            ApiV1AlertsDiscoverCreateArchivedErrorComponent | ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1AlertsDiscoverCreateBlockErrorComponent | ApiV1AlertsDiscoverCreateCategoryErrorComponent |
            ApiV1AlertsDiscoverCreateCriticalityErrorComponent | ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent |
            ApiV1AlertsDiscoverCreateDebugModeErrorComponent | ApiV1AlertsDiscoverCreateDisplayNameErrorComponent |
            ApiV1AlertsDiscoverCreateExternalUrlErrorComponent | ApiV1AlertsDiscoverCreateFingerprintErrorComponent |
            ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent | ApiV1AlertsDiscoverCreateK8SAppErrorComponent |
            ApiV1AlertsDiscoverCreateK8SClusterErrorComponent | ApiV1AlertsDiscoverCreateKindErrorComponent |
            ApiV1AlertsDiscoverCreateLabelsErrorComponent | ApiV1AlertsDiscoverCreateLastSeenErrorComponent |
            ApiV1AlertsDiscoverCreateMessageErrorComponent | ApiV1AlertsDiscoverCreateNameErrorComponent |
            ApiV1AlertsDiscoverCreateNamespaceErrorComponent | ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1AlertsDiscoverCreatePanelUrlErrorComponent | ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent |
            ApiV1AlertsDiscoverCreatePodErrorComponent | ApiV1AlertsDiscoverCreateProviderErrorComponent |
            ApiV1AlertsDiscoverCreateProviderIdErrorComponent | ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent |
            ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent | ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent |
            ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent | ApiV1AlertsDiscoverCreateSlaTargetErrorComponent |
            ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent | ApiV1AlertsDiscoverCreateSloTargetErrorComponent |
            ApiV1AlertsDiscoverCreateStatusErrorComponent | ApiV1AlertsDiscoverCreateSuppressedErrorComponent |
            ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent | ApiV1AlertsDiscoverCreateTitleErrorComponent |
            ApiV1AlertsDiscoverCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsDiscoverCreateAlertRouterErrorComponent
        | ApiV1AlertsDiscoverCreateAnnotationsErrorComponent
        | ApiV1AlertsDiscoverCreateArchivedAtErrorComponent
        | ApiV1AlertsDiscoverCreateArchivedErrorComponent
        | ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1AlertsDiscoverCreateBlockErrorComponent
        | ApiV1AlertsDiscoverCreateCategoryErrorComponent
        | ApiV1AlertsDiscoverCreateCriticalityErrorComponent
        | ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent
        | ApiV1AlertsDiscoverCreateDebugModeErrorComponent
        | ApiV1AlertsDiscoverCreateDisplayNameErrorComponent
        | ApiV1AlertsDiscoverCreateExternalUrlErrorComponent
        | ApiV1AlertsDiscoverCreateFingerprintErrorComponent
        | ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent
        | ApiV1AlertsDiscoverCreateK8SAppErrorComponent
        | ApiV1AlertsDiscoverCreateK8SClusterErrorComponent
        | ApiV1AlertsDiscoverCreateKindErrorComponent
        | ApiV1AlertsDiscoverCreateLabelsErrorComponent
        | ApiV1AlertsDiscoverCreateLastSeenErrorComponent
        | ApiV1AlertsDiscoverCreateMessageErrorComponent
        | ApiV1AlertsDiscoverCreateNameErrorComponent
        | ApiV1AlertsDiscoverCreateNamespaceErrorComponent
        | ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1AlertsDiscoverCreatePanelUrlErrorComponent
        | ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1AlertsDiscoverCreatePodErrorComponent
        | ApiV1AlertsDiscoverCreateProviderErrorComponent
        | ApiV1AlertsDiscoverCreateProviderIdErrorComponent
        | ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent
        | ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent
        | ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1AlertsDiscoverCreateSlaTargetErrorComponent
        | ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1AlertsDiscoverCreateSloTargetErrorComponent
        | ApiV1AlertsDiscoverCreateStatusErrorComponent
        | ApiV1AlertsDiscoverCreateSuppressedErrorComponent
        | ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1AlertsDiscoverCreateTitleErrorComponent
        | ApiV1AlertsDiscoverCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_discover_create_alert_router_error_component import (
            ApiV1AlertsDiscoverCreateAlertRouterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_annotations_error_component import (
            ApiV1AlertsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_archived_at_error_component import (
            ApiV1AlertsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_archived_error_component import (
            ApiV1AlertsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_archived_reason_error_component import (
            ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_category_error_component import (
            ApiV1AlertsDiscoverCreateCategoryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_criticality_error_component import (
            ApiV1AlertsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_dashboard_url_error_component import (
            ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_debug_mode_error_component import (
            ApiV1AlertsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_display_name_error_component import (
            ApiV1AlertsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_external_url_error_component import (
            ApiV1AlertsDiscoverCreateExternalUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_fingerprint_error_component import (
            ApiV1AlertsDiscoverCreateFingerprintErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_generator_url_error_component import (
            ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_k8s_app_error_component import (
            ApiV1AlertsDiscoverCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_k8s_cluster_error_component import (
            ApiV1AlertsDiscoverCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_kind_error_component import (
            ApiV1AlertsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_labels_error_component import (
            ApiV1AlertsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_last_seen_error_component import (
            ApiV1AlertsDiscoverCreateLastSeenErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_message_error_component import (
            ApiV1AlertsDiscoverCreateMessageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_name_error_component import (
            ApiV1AlertsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_namespace_error_component import (
            ApiV1AlertsDiscoverCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_non_field_errors_error_component import (
            ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_panel_url_error_component import (
            ApiV1AlertsDiscoverCreatePanelUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_platform_service_error_component import (
            ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_pod_error_component import (
            ApiV1AlertsDiscoverCreatePodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_provider_error_component import (
            ApiV1AlertsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_provider_id_error_component import (
            ApiV1AlertsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_provider_reference_error_component import (
            ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_reconciliation_enabled_error_component import (
            ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_silence_ends_at_error_component import (
            ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_silence_url_error_component import (
            ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_sla_availability_error_component import (
            ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_sla_target_error_component import (
            ApiV1AlertsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_slo_availability_error_component import (
            ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_slo_target_error_component import (
            ApiV1AlertsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_status_error_component import (
            ApiV1AlertsDiscoverCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_suppressed_error_component import (
            ApiV1AlertsDiscoverCreateSuppressedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_target_availability_error_component import (
            ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_title_error_component import (
            ApiV1AlertsDiscoverCreateTitleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_tolerations_error_component import (
            ApiV1AlertsDiscoverCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateMessageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateLastSeenErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSuppressedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreatePodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreatePanelUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsDiscoverCreateK8SAppErrorComponent):
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
        from ..models.api_v1_alerts_discover_create_alert_router_error_component import (
            ApiV1AlertsDiscoverCreateAlertRouterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_annotations_error_component import (
            ApiV1AlertsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_archived_at_error_component import (
            ApiV1AlertsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_archived_error_component import (
            ApiV1AlertsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_archived_reason_error_component import (
            ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_block_error_component import (
            ApiV1AlertsDiscoverCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_category_error_component import (
            ApiV1AlertsDiscoverCreateCategoryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_criticality_error_component import (
            ApiV1AlertsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_dashboard_url_error_component import (
            ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_debug_mode_error_component import (
            ApiV1AlertsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_display_name_error_component import (
            ApiV1AlertsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_external_url_error_component import (
            ApiV1AlertsDiscoverCreateExternalUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_fingerprint_error_component import (
            ApiV1AlertsDiscoverCreateFingerprintErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_generator_url_error_component import (
            ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_k8s_app_error_component import (
            ApiV1AlertsDiscoverCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_k8s_cluster_error_component import (
            ApiV1AlertsDiscoverCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_kind_error_component import (
            ApiV1AlertsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_labels_error_component import (
            ApiV1AlertsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_last_seen_error_component import (
            ApiV1AlertsDiscoverCreateLastSeenErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_message_error_component import (
            ApiV1AlertsDiscoverCreateMessageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_name_error_component import (
            ApiV1AlertsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_namespace_error_component import (
            ApiV1AlertsDiscoverCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_non_field_errors_error_component import (
            ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_panel_url_error_component import (
            ApiV1AlertsDiscoverCreatePanelUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_platform_service_error_component import (
            ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_pod_error_component import (
            ApiV1AlertsDiscoverCreatePodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_provider_error_component import (
            ApiV1AlertsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_provider_id_error_component import (
            ApiV1AlertsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_provider_reference_error_component import (
            ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_reconciliation_enabled_error_component import (
            ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_silence_ends_at_error_component import (
            ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_silence_url_error_component import (
            ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_sla_availability_error_component import (
            ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_sla_target_error_component import (
            ApiV1AlertsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_slo_availability_error_component import (
            ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_slo_target_error_component import (
            ApiV1AlertsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_status_error_component import (
            ApiV1AlertsDiscoverCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_suppressed_error_component import (
            ApiV1AlertsDiscoverCreateSuppressedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_target_availability_error_component import (
            ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_title_error_component import (
            ApiV1AlertsDiscoverCreateTitleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_discover_create_tolerations_error_component import (
            ApiV1AlertsDiscoverCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsDiscoverCreateAlertRouterErrorComponent
                | ApiV1AlertsDiscoverCreateAnnotationsErrorComponent
                | ApiV1AlertsDiscoverCreateArchivedAtErrorComponent
                | ApiV1AlertsDiscoverCreateArchivedErrorComponent
                | ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1AlertsDiscoverCreateBlockErrorComponent
                | ApiV1AlertsDiscoverCreateCategoryErrorComponent
                | ApiV1AlertsDiscoverCreateCriticalityErrorComponent
                | ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent
                | ApiV1AlertsDiscoverCreateDebugModeErrorComponent
                | ApiV1AlertsDiscoverCreateDisplayNameErrorComponent
                | ApiV1AlertsDiscoverCreateExternalUrlErrorComponent
                | ApiV1AlertsDiscoverCreateFingerprintErrorComponent
                | ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent
                | ApiV1AlertsDiscoverCreateK8SAppErrorComponent
                | ApiV1AlertsDiscoverCreateK8SClusterErrorComponent
                | ApiV1AlertsDiscoverCreateKindErrorComponent
                | ApiV1AlertsDiscoverCreateLabelsErrorComponent
                | ApiV1AlertsDiscoverCreateLastSeenErrorComponent
                | ApiV1AlertsDiscoverCreateMessageErrorComponent
                | ApiV1AlertsDiscoverCreateNameErrorComponent
                | ApiV1AlertsDiscoverCreateNamespaceErrorComponent
                | ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1AlertsDiscoverCreatePanelUrlErrorComponent
                | ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1AlertsDiscoverCreatePodErrorComponent
                | ApiV1AlertsDiscoverCreateProviderErrorComponent
                | ApiV1AlertsDiscoverCreateProviderIdErrorComponent
                | ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent
                | ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent
                | ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1AlertsDiscoverCreateSlaTargetErrorComponent
                | ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1AlertsDiscoverCreateSloTargetErrorComponent
                | ApiV1AlertsDiscoverCreateStatusErrorComponent
                | ApiV1AlertsDiscoverCreateSuppressedErrorComponent
                | ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1AlertsDiscoverCreateTitleErrorComponent
                | ApiV1AlertsDiscoverCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_0 = (
                        ApiV1AlertsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_1 = (
                        ApiV1AlertsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_2 = (
                        ApiV1AlertsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_3 = (
                        ApiV1AlertsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_4 = (
                        ApiV1AlertsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_5 = (
                        ApiV1AlertsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_6 = (
                        ApiV1AlertsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_7 = (
                        ApiV1AlertsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_8 = (
                        ApiV1AlertsDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_9 = (
                        ApiV1AlertsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_10 = (
                        ApiV1AlertsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_11 = (
                        ApiV1AlertsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_12 = (
                        ApiV1AlertsDiscoverCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_13 = (
                        ApiV1AlertsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_14 = (
                        ApiV1AlertsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_15 = (
                        ApiV1AlertsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_16 = (
                        ApiV1AlertsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_17 = (
                        ApiV1AlertsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_18 = (
                        ApiV1AlertsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_19 = (
                        ApiV1AlertsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_20 = (
                        ApiV1AlertsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_21 = (
                        ApiV1AlertsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_22 = (
                        ApiV1AlertsDiscoverCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_23 = (
                        ApiV1AlertsDiscoverCreateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_24 = (
                        ApiV1AlertsDiscoverCreateFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_25 = (
                        ApiV1AlertsDiscoverCreateExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_26 = (
                        ApiV1AlertsDiscoverCreateMessageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_27 = (
                        ApiV1AlertsDiscoverCreateLastSeenErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_28 = (
                        ApiV1AlertsDiscoverCreateSuppressedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_29 = (
                        ApiV1AlertsDiscoverCreatePodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_30 = (
                        ApiV1AlertsDiscoverCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_31 = (
                        ApiV1AlertsDiscoverCreateCategoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_32 = (
                        ApiV1AlertsDiscoverCreateDashboardUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_33 = (
                        ApiV1AlertsDiscoverCreatePanelUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_34 = (
                        ApiV1AlertsDiscoverCreateSilenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_35 = (
                        ApiV1AlertsDiscoverCreateSilenceEndsAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_36 = (
                        ApiV1AlertsDiscoverCreateGeneratorUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_37 = (
                        ApiV1AlertsDiscoverCreateAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_38 = (
                        ApiV1AlertsDiscoverCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_discover_create_error_type_39 = (
                        ApiV1AlertsDiscoverCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_discover_create_error_type_40 = (
                    ApiV1AlertsDiscoverCreateBlockErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alerts_discover_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_discover_create_validation_error.additional_properties = d
        return api_v1_alerts_discover_create_validation_error

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
