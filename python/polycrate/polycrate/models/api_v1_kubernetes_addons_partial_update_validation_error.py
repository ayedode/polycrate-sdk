from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addons_partial_update_actual_availability_error_component import (
        ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_allow_multiple_error_component import (
        ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_annotations_error_component import (
        ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_archived_at_error_component import (
        ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_archived_error_component import (
        ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_archived_reason_error_component import (
        ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_block_name_error_component import (
        ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_catalogue_app_error_component import (
        ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_criticality_error_component import (
        ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_debug_mode_error_component import (
        ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_default_block_config_template_error_component import (
        ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_default_version_error_component import (
        ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_display_name_error_component import (
        ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_enforcement_error_component import (
        ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_is_default_error_component import (
        ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_kind_error_component import (
        ApiV1KubernetesAddonsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_labels_error_component import (
        ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_name_error_component import (
        ApiV1KubernetesAddonsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_order_error_component import (
        ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_platform_service_error_component import (
        ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_provider_error_component import (
        ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_provider_id_error_component import (
        ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_provider_reference_error_component import (
        ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_scope_error_component import (
        ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_scope_expressions_error_component import (
        ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_sla_availability_error_component import (
        ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_sla_target_error_component import (
        ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_slo_availability_error_component import (
        ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_slo_target_error_component import (
        ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_target_availability_error_component import (
        ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_partial_update_template_block_error_component import (
        ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonsPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesAddonsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent | ApiV1KubernetesAddonsPartialUpdateKindErrorComponent
            | ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent | ApiV1KubernetesAddonsPartialUpdateNameErrorComponent
            | ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent |
            ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateKindErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateNameErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent
        | ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addons_partial_update_actual_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_allow_multiple_error_component import (
            ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_annotations_error_component import (
            ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_archived_at_error_component import (
            ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_archived_error_component import (
            ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_archived_reason_error_component import (
            ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_block_name_error_component import (
            ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_catalogue_app_error_component import (
            ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_criticality_error_component import (
            ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_debug_mode_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_default_version_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_display_name_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_is_default_error_component import (
            ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_kind_error_component import (
            ApiV1KubernetesAddonsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_labels_error_component import (
            ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_name_error_component import (
            ApiV1KubernetesAddonsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_order_error_component import (
            ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_platform_service_error_component import (
            ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_provider_error_component import (
            ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_provider_id_error_component import (
            ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_provider_reference_error_component import (
            ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_scope_error_component import (
            ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_scope_expressions_error_component import (
            ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_sla_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_sla_target_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_slo_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_slo_target_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_target_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_template_block_error_component import (
            ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent):
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
        from ..models.api_v1_kubernetes_addons_partial_update_actual_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_allow_multiple_error_component import (
            ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_annotations_error_component import (
            ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_archived_at_error_component import (
            ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_archived_error_component import (
            ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_archived_reason_error_component import (
            ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_block_name_error_component import (
            ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_catalogue_app_error_component import (
            ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_criticality_error_component import (
            ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_debug_mode_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_default_version_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_display_name_error_component import (
            ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_enforcement_error_component import (
            ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_is_default_error_component import (
            ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_kind_error_component import (
            ApiV1KubernetesAddonsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_labels_error_component import (
            ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_name_error_component import (
            ApiV1KubernetesAddonsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_order_error_component import (
            ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_platform_service_error_component import (
            ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_provider_error_component import (
            ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_provider_id_error_component import (
            ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_provider_reference_error_component import (
            ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_scope_error_component import (
            ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_scope_expressions_error_component import (
            ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_sla_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_sla_target_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_slo_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_slo_target_error_component import (
            ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_target_availability_error_component import (
            ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_partial_update_template_block_error_component import (
            ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateKindErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateNameErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent
                | ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_0 = (
                        ApiV1KubernetesAddonsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_1 = (
                        ApiV1KubernetesAddonsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_2 = (
                        ApiV1KubernetesAddonsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_3 = (
                        ApiV1KubernetesAddonsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_4 = (
                        ApiV1KubernetesAddonsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_5 = (
                        ApiV1KubernetesAddonsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_6 = (
                        ApiV1KubernetesAddonsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_7 = (
                        ApiV1KubernetesAddonsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_8 = (
                        ApiV1KubernetesAddonsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_9 = (
                        ApiV1KubernetesAddonsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_10 = (
                        ApiV1KubernetesAddonsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_11 = (
                        ApiV1KubernetesAddonsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_12 = (
                        ApiV1KubernetesAddonsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_13 = (
                        ApiV1KubernetesAddonsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_14 = (
                        ApiV1KubernetesAddonsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_15 = (
                        ApiV1KubernetesAddonsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_16 = (
                        ApiV1KubernetesAddonsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_17 = (
                        ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_18 = (
                        ApiV1KubernetesAddonsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_19 = (
                        ApiV1KubernetesAddonsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_20 = (
                        ApiV1KubernetesAddonsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_21 = (
                        ApiV1KubernetesAddonsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_22 = (
                        ApiV1KubernetesAddonsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_23 = (
                        ApiV1KubernetesAddonsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_24 = (
                        ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_25 = (
                        ApiV1KubernetesAddonsPartialUpdateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_26 = (
                        ApiV1KubernetesAddonsPartialUpdateDefaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_27 = (
                        ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_28 = (
                        ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_29 = (
                        ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_30 = (
                        ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_31 = (
                        ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_32 = (
                        ApiV1KubernetesAddonsPartialUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_33 = (
                    ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addons_partial_update_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addons_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addons_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_addons_partial_update_validation_error

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
