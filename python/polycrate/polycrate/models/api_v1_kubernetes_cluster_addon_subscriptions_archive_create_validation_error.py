from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_actual_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_addon_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_annotations_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_at_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_reason_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_config_template_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_criticality_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_debug_mode_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_display_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_k8s_cluster_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_kind_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_labels_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_order_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_platform_service_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_id_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_reference_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_scope_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_sla_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_sla_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_slo_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_slo_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_target_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_version_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent
            ):
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
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_order_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_archive_create_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_0 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNonFieldErrorsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_1 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_2 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_3 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_4 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_5 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_6 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_7 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderReferenceErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_8 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_9 = ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_10 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_11 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreatePlatformServiceErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_12 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_13 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_14 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_15 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_16 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedReasonErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_17 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_18 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateTargetAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_19 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateActualAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_20 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_21 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSloAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_22 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_23 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateSlaAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_24 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_25 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_26 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_27 = (
                        ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_28 = ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockConfigTemplateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_29 = (
                    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateOrderErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_cluster_addon_subscriptions_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_cluster_addon_subscriptions_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_cluster_addon_subscriptions_archive_create_validation_error

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
